import argparse
import logging
import multiprocessing as mp
import os
import queue
import sys
import traceback
from pathlib import Path
from typing import Optional

from kaitaistruct import KaitaiStructError

from .. import filetypes
from ..dumputil import DataOutput, fileparse, get_contenthash
from ..filters import check_filtered
from .pathwalk import pathwalk


# A single parallel task -- process a single file, write the output
class WalkTask(object):
    def __init__(self, args: argparse.Namespace, infile: Path, outfile: Path, overwrite: bool):
        self.args = args
        self.infile = infile
        self.outfile = outfile
        self.overwrite = overwrite

    def __call__(self):
        self.args.resolve = False
        try:
            walk_file(self.args, self.infile, self.outfile, self.overwrite)

            # return f"ok: {self.infile}"
            return None
        except (OSError, EOFError, KaitaiStructError) as e:
            # logger.warning(f"error while processing: {e}")
            self.outfile.unlink(missing_ok=True)
            return f"fail: {self.infile} - {e}"
        except Exception:
            tb = traceback.format_exc()
            return f"unknown: {self.infile} - {tb}"

    def __str__(self):
        return str(self.infile)


# Our parallel worker class, handles individual task dispatch (one
# task == one file to process))
class WalkWorker(mp.Process):
    def __init__(self, task_queue: 'mp.Queue[Optional[WalkTask]]', result_queue: 'mp.Queue[str]',
                 timeout: float = 60.0):
        mp.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
        self.timeout = timeout

    def run(self):
        proc_name = self.name

        while True:
            try:
                next_task = self.task_queue.get(timeout=self.timeout)
            except queue.Empty:
                print(f"{proc_name}: Timeout, exiting", file=sys.stderr)
                self.result_queue.put(f"error: {proc_name} timed out")

            if next_task is None:
                # Time to exit
                print(f"{proc_name}: Exiting", file=sys.stderr)
                self.task_queue.task_done()
                break

            answer = next_task()
            self.task_queue.task_done()
            if answer:
                self.result_queue.put(answer)


def walk_file(args: argparse.Namespace, infile: Path, outfile: Path, overwrite: bool) -> None:
    logger = logging.getLogger("pathwalk")

    if not overwrite and outfile.exists():
        logger.debug(f"skipping due to existing output file: {infile}")
        return

    outfile.parent.mkdir(parents=True, exist_ok=True)

    logger.debug(f"processing input file: {infile}")
    if args.verbose:
        print(f"processing: {infile}", file=sys.stderr)

    target = fileparse(infile)
    with DataOutput(str(outfile)) as out:
        if not check_filtered(args, "/contenthash"):
            h = get_contenthash(infile)
            out.write(f"/contenthash = {h}")

        for line in pathwalk(args, target, ""):
            out.write(line)


# FIXME: How do we deal with errors and such?
def cmd_bulkwalk(args):
    logger = logging.getLogger("bulkwalk")

    if not args.output:
        print("ERROR: bulkwalk requires --output be specified", file=sys.stderr)
        return 64  # os.EX_USAGE

    # FIXME: Should we just create it if it doesn't exist?
    outdir = Path(args.output).resolve(strict=False)
    if not outdir.exists() or not outdir.is_dir():
        print(f"ERROR: doesn't exist or isn't a directory: {outdir}")
        return 65  # os.EX_DATAERR

    indir = Path(args.file).resolve(strict=False)
    if not indir.exists() or not indir.is_dir():
        print(f"ERROR: doesn't exist or isn't a directory: {indir}")
        return 65  # os.EX_DATAERR

    supported = filetypes.get_supported()

    mp.set_start_method('spawn')
    tasks: mp.JoinableQueue[Optional[WalkTask]] = mp.JoinableQueue(maxsize=500)
    results: mp.Queue[str] = mp.Queue()

    num_workers = mp.cpu_count() * 1

    print(f"Creating {num_workers} workers...", file=sys.stderr)
    workers = [WalkWorker(tasks, results) for i in range(num_workers)]

    for w in workers:
        w.start()

    for dirpath, _dirs, files in os.walk(indir):
        dp = Path(dirpath)
        outsubpath = dp.relative_to(indir)

        for file in files:
            inpath = dp / file
            ext = inpath.suffix.lower()

            if ext not in supported:
                logger.debug(f"skipping file with unknown type: {inpath}")
                continue

            if args.bulk_type and f".{args.bulk_type}" != ext:
                logger.debug(f"skipping file with non-requested type: {inpath}")
                continue

            # supported/requested filetype, so process it
            out_file = inpath.name + ".txt"
            outpath = outdir / outsubpath / out_file

            # Ugh, finally done with path juggling, maybe we can actually,
            # y'know, process something?
            # try:
            #     walk_file(args, inpath, outpath, args.bulk_overwrite, cachecon)
            # except (OSError, EOFError, KaitaiStructError) as e:
            #     logger.warning(f"error while processing: {e}")
            #     outpath.unlink(missing_ok=True)
            tasks.put(WalkTask(args, inpath, outpath, args.bulk_overwrite))

    # Tell each consumer to die, since we're out of stuff
    for i in range(num_workers):
        tasks.put(None)

    # wait for them all to finish
    tasks.join()

    while True:
        try:
            result = results.get_nowait()
        except queue.Empty:
            break

        print(f"Result: {result}", file=sys.stderr)


    return 0
