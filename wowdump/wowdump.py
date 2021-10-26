import argparse
import csv
import hashlib
import json
import os
import pathlib
import re
import sys
import time

from kaitaistruct import KaitaiStruct, KaitaiStructError
from typing import Union, Optional, Iterable, TextIO

import logging
from ppretty import ppretty

from . import filetypes
# from .filetypes import load_wowfile, get_supported
from .dumputil import ktype, kttree, whatis
from .simplifiers import check_simplify

# We can run without, we'll just be slow
try:
    import sqlite3
except ImportError:
    pass

# This script is what's known as "awful". It's brute force. It does
# everything wrong. It probably doesn't even taste like chocolate.
# But should at least give a baseline for dumping interesting info
# out of interesting files, even if it *is* garbage at the moment.
#
# Also, did I mention it's garbage?

class DataOutput(object):
    fileName: Optional[Union[str, os.PathLike]] = None
    fileHandle: TextIO
    is_stdout: bool

    def __init__(self, fn: Optional[Union[str, os.PathLike]]):
        self.fileName = fn

    def __enter__(self):
        if self.fileName is not None:
            self.fileHandle = open(self.fileName, "w")
            self.is_stdout = False
        else:
            self.fileHandle = sys.stdout
            self.is_stdout = True

        return self

    def __exit__(self, _ex_type, _ex_value, _ex_traceback):
        # only close if not stdout
        if not self.is_stdout:
            self.fileHandle.close()

        return False

    def write(self, outstr: str):
        print(outstr, file=self.fileHandle, flush=self.is_stdout)


# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_TARGET = "testfiles/staff_2h_draenorcrafted_d_02_c.m2"
CASCDIR = None
DATADIR = os.path.dirname(os.path.realpath(__file__))


global args

def get_contenthash(filename: Union[str, os.PathLike]):
    with open(filename, "rb") as f:
        h = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            h.update(chunk)
            chunk = f.read(8192)

    return h.hexdigest()


# places to look for file:
#   - next to original file
#   - maybe some directory relative to original file
#   - some configured CASC path
# def find_related(filepath, base):
#     if os.path.isfile(base):
#         base = os.path.dirname(base)

#     filename = os.path.basename(filepath)
#     check = os.path.join(base, filename)
#     if os.path.isfile(check):
#         return check

#     if CASCDIR:
#         check = os.path.join(CASCDIR, filepath)
#         if os.path.isfile(check):
#             return check

#     return None

# When dealing with big files with a lot of fields, we end up spending a
# good bit of time filtering through the various attributes on each object
# to find the ones we need to actually descend through and such. By pulling
# that filtering logic into a separate funciton that caches the results, we
# can gain some performance on big objects (and make the main walk function
# a little easier to read). Some testing on `valeera.m2` suggests that on
# large files dumped with `--geometry` save about 5% runtime. Definitely
# not great, but no real downsides, either. At least, don't think so. All
# the unit tests pass!
#
# FIXME: how much overhead to passing objects here? Is there any better way?
attrcache = {}

def cacheattrs(obj):
    t = type(obj)

    if t in attrcache:
        return attrcache[t]

    cacheentry = []

    obj_keys = dir(obj)

    for k in obj_keys:
        if k[0] == "_":
            continue

        # FIXME: figure out what to do with m2track
        if k == "m2array_type":
            continue

        v = getattr(obj, k)

        # FIXME: Can we economize here, any?
        kt = ktype(v)
        if kt == "skip":  # class, method, datatype
            continue

        # looks like k is something we want to keep
        cacheentry.append(k)

    attrcache[t] = cacheentry
    return cacheentry


def pathwalk(obj: KaitaiStruct, path: str, cachecon) -> Iterable[str]:
    lgsimplify = logging.getLogger("simplify")
    lgdisp = logging.getLogger("disposition")

    logger = logging.getLogger()
    logger.debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    # I don't thiiiiiiiink we get called with an object that isn't a
    # kaitai type, so even though we used to have to figure out object
    # type here, seems like we don't, at this point?
    obj_keys = cacheattrs(obj)


    # if path == "/skin/bulkes/0":
    #     print("breakpoint")

    for k in obj_keys:
        workpath = f"{path}/{k}"

        # if workpath == "/model/vertices":
        #     print("breakpoint")

        logger.debug(f"getattr {k} from obj type {type(obj)}")
        v = getattr(obj, k)

        kt = ktype(v)

        logger.debug(f"checking for array elision for {workpath}")
        # this is probably a code smell, if not worse. If our current level
        # isn't geometry, but we add a '/0' to it and it is, that means it's
        # the very top of a geometry tree, and we can save ourselves the
        # effort of descending into it (and thus reading & parsing it) by
        # just escaping now.
        if not args.geometry and not geometry_path(workpath) and geometry_path(f"{workpath}/0"):
            if not check_filtered(workpath):
                yield f"{workpath}/... = [geometry data elided, use --geometry to include]"
            continue

        # if we have ofs_xxx or num_xxx, and *also* just have xxx,
        # we don't need the offset/size anymore
        if args.hide_unneeded and isinstance(k, str) and (k.startswith("ofs_") or k.startswith("num_")):
            s = k[len("ofs_"):]
            if s in obj_keys:
                continue

        # FIXME: Where is the best place for simplifiers? Here?
        lgsimplify.debug(f"checking simplifier for {workpath}")
        s = check_simplify(workpath) if args.simplify else None
        if s:
            lgsimplify.debug(f"using simplifier for {workpath}")

            # if getting simplified, it's a "final" path, so check filtering
            if check_filtered(workpath):
                continue

            # FIXME: this feels sloppy
            if kt == "base" or kt == "list":
                simplified = s(v, obj, cachecon, args)
            else:
                simplified = s(v, obj, cachecon, args)
            if simplified is not None:
                yield f"{workpath} = {simplified}"

            # We either simplified w/ output, or simplified out of existence.
            # either way, move on
            continue

        if kt == "list":
            lgdisp.debug(f"{workpath}[] --> array processing (len {len(v)})")

            # everything in an array shoooould have the same contents, so no
            # benefit to checking for a simplifier match for each, just check
            # for the first element and keep it
            s = check_simplify(f"{workpath}/0") if args.simplify else None

            for i, el in enumerate(v):
                arraypath = f"{workpath}/{i}"
                elt = ktype(el)

                # if --geometry is specified, we still want to limit it to just
                # our array limit of entries, unless we've set arraylimit=0
                if geometry_path(arraypath) and args.arraylimit > 0 and i >= args.arraylimit:
                    logger.debug(
                        f"eliding remaining geometry entries for {workpath}")
                    if not check_filtered(arraypath):
                        remaining = len(v) - args.arraylimit
                        yield f"{workpath}/... = [{remaining} elided of {len(v)} total]"
                    break

                # if we're going to elide all arrays (via --elide-all), check
                # that, too, and bail if we've hit the limit
                if args.elide_all and args.arraylimit > 0 and i >= args.arraylimit:
                    logger.debug(
                        f"eliding remaining array entries for {workpath}")
                    if not check_filtered(arraypath):
                        remaining = len(v) - args.arraylimit
                        yield f"{workpath}/... = [{remaining} elided of {len(v)} total]"
                    break

                # FIXME: dedupe dedupe
                # s = check_simplify(arraypath) if args.simplify else None
                if s:
                    lgsimplify.debug(f"using simplifier for {arraypath}")

                    # if getting simplified, it's a "final" path, so check filtering
                    if check_filtered(arraypath):
                        continue

                    lgsimplify.debug(
                        f"array simplify type: {type(el)}   value: {el}")
                    # FIXME: this feels sloppy
                    if elt == "base" or elt == "list":
                        simplified = s(el, v, cachecon, args)
                    else:
                        simplified = s(el, v, cachecon, args)
                    if simplified is not None:
                        yield f"{arraypath} = {simplified}"

                    # We either simplified w/ output, or simplified out of existence.
                    # either way, move on
                    continue

                # if elt in [int, float, str]:
                if elt == "base":
                    # we're at a final path, check filtering
                    if check_filtered(workpath):
                        continue

                    if isinstance(el, str):
                        el = el.rstrip("\0")
                    lgdisp.debug(f"array {arraypath} --> final ({el})")
                    yield f"{arraypath} = {el}"
                else:
                    lgdisp.debug(f"{arraypath} --> array descent")
                    yield from pathwalk(el, arraypath, cachecon)

        elif kt == "kaitai":
            # FIXME: I think we're supposed to do one of these without the {k}
            if k == "data":
                lgdisp.debug(f"{workpath} --> kaitai data descent")
                yield from pathwalk(v, workpath, cachecon)
            else:
                lgdisp.debug(f"{workpath} --> kaitai descent type {type(k)}")
                # debug(f"recursing kaitai value, type: {type(k)}")
                yield from pathwalk(v, workpath, cachecon)

        elif kt == "base":
            # we're at a final path, check filtering
            if check_filtered(workpath):
                continue

            if isinstance(v, str):
                v = v.rstrip("\0")

            lgdisp.debug(f"{workpath} --> final ({v})")
            yield f"{workpath} = {v}"

        else:
            lgdisp.debug(f"{workpath} --> descend (type {type(v)}")
            yield from pathwalk(v, workpath, cachecon)

# for maybe speeding up logging when a debug level is disabled:
#
# class Lazy(object):
#     def __init__(self,func):
#         self.func=func
#     def __str__(self):
#         return self.func()
#
# logger.debug(Lazy(lambda: time.sleep(20)))
#
# logger.info(Lazy(lambda: "Stupid log message " + ' '.join([str(i) for i in range(20)])))


# Caching bits (yeah, they're ugly)
# or maybe type of os.PathLike for cache_open
# FIXME: move caching bits to separate module
# FIXME: needs locking for cache rebuild
def cache_open(dbfile: Union[str, os.PathLike]):
    if "sqlite3" not in sys.modules:
        print("WARNING: sqlite not available, caching disabled", file=sys.stderr)
        return None

    # FIXME: can we do better than a global variable?
    cachecon = sqlite3.connect(dbfile)

    return cachecon


def cache_prepare(args):
    log = logging.getLogger()

    if not args.resolve:
        # print("INFO: not resolving, not initializing cache", file=sys.stderr)
        return None
    elif not os.path.exists(args.listfile):
        log.warning(
            f"{args.listfile} does not exist, not resolving fileids")
        return None
    else:
        cachefile = f"{args.listfile}.cache"
        if os.path.exists(cachefile) and (os.path.getmtime(args.listfile) <= os.path.getmtime(cachefile)):
            # print("INFO: fileid cache up to date, not updating", file=sys.stderr)
            return cache_open(cachefile)
        else:
            cachecon = cache_open(cachefile)
            cache_fileids(args.listfile, cachecon)
            return cachecon


def cache_fileids(listfile: Union[str, os.PathLike], cachecon) -> None:
    # Don't have the cache open, so can't cache anything
    if not cachecon:
        return

    print("INFO: newer listfile available, updating fileid cache", file=sys.stderr)
    started = time.time()

    cur = cachecon.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS file_ids (
            id INTEGER NOT NULL PRIMARY KEY,
            name VARCHAR
        );
        """)

    # Make sure it's empty -- it's probably faster to just reload everything
    # rather than check if each indiviual row needs updating anyhow
    cur.execute("DELETE FROM file_ids;")

    with open(listfile, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        to_db = [(row[0], row[1]) for row in reader]

    cur.executemany("INSERT INTO file_ids (id, name) VALUES (?, ?);", to_db)
    cachecon.commit()

    runtime = time.time() - started
    print(
        f"INFO: fileid cache successfully rebuilt in {runtime:.2f}s", file=sys.stderr)


# There's probably a way better way to do this.
# filter_regex_cache = { }
# def regex_cache(re_str):
#     if not re_str.startswith("/") or not re_str.endswith("/"):
#         return None

#     if re_str in filter_regex_cache:
#         return filter_regex_cache[re_str]

#     re_compiled = re.compile(re_str, re.IGNORECASE)
#     filter_regex_cache[re_str] = re_compiled
#     return re_compiled

# rudamentary filtering
#
# behavior depends on whether keep or discard filters are provided,
# or both.
#
# no filter -- allow all
# only keep -- discard all but matching
# only discard --  keep all but matching
# both -- allow 'keep' matches, then discard all matching, then allow remaining
def check_filtered(path: str) -> bool:
    if len(args.filters_keep) == 0 and len(args.filters_discard) == 0:
        return False

    # Always do the 'keep' first, if they exist, since if there's a match, we
    # don't care after that.
    if len(args.filters_keep) > 0:
        for filter in args.filters_keep:
            # r = regex_cache(filter)
            # if r and r.search(path):
            #     return False

            # print(f"check filter {filter} vs {path}")
            # if path.startswith(filter):
            if filter in path:
                return False

    if len(args.filters_discard):
        for filter in args.filters_discard:
            # r = regex_cache(filter)
            # if r and r.search(path):
            #     return True

            # if path.startswith(filter):
            if filter in path:
                return True

    # If we're here, we didn't match anything, so check which of the
    # combinations of above exists
    if len(args.filters_keep) > 0 and len(args.filters_discard) > 0:
        # We survived both filters, keep it
        return False

    if len(args.filters_keep) > 0:
        # we only wanted to keep some, so get rid of the rest
        return True

    # otherwise, we were discard-only, so don't filter anything remaining
    return False


# Given a path, check to see if it's one we want to normally elide (because
# it's geometry-related and thus probably really long and spammy with minimal
# value).
#
# FIXME: It'd be great if we didn't have to maintain the regex list by hand.
geom_path_re = re.compile(
    r"/(model|skin|chunk_data)/(bones|polys|indices|vertices|normals|tex_coords|bspnodes|vertex_colors|node_face_indices)/\d+$")

def geometry_path(path):
    if geom_path_re.search(path):
        return True


class NegateAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'no')

def parse_arguments(argv, loggers):
    parser = argparse.ArgumentParser(
        prog="wowdump",
        description="A tool for dumping the information out of WoW files",
    )

    #
    # commands
    #
    cmdgroup = parser.add_argument_group(title="execution modes")
    cmdgroup.add_argument(
        '--pathwalk',
        action='store_const',
        const="pathwalk",
        dest="mode",
        default="pathwalk",
        help="pathwalk mode (default)",
    )

    cmdgroup.add_argument(
        '--bulkwalk',
        action='store_const',
        const="bulkwalk",
        dest="mode",
        help="bulk output pathwalk",
    )

    cmdgroup.add_argument(
        '--json',
        action='store_const',
        const="json",
        dest="mode",
        help="json dump",
    )

    cmdgroup.add_argument(
        '--raw',
        action='store_const',
        const="raw",
        dest="mode",
        help="raw kaitai dump",
    )

    #
    # everything else
    #

    parser.add_argument(
        "--verbose",
        action='store_const',
        const=True,
        default=False,
        # help="help text",
    )

    parser.add_argument(
        "--debug",
        action='store_const',
        const=True,
        default=False,
        # help="help text",
    )

    for lg in loggers:
        parser.add_argument(
            f"--debug-{lg}",
            action="store_const",
            const=True,
            default=False,
            # help = "whatever",
        )

    levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    parser.add_argument(
        "--log-level",
        default='INFO',
        choices=levels,
    )

    parser.add_argument(
        "--showtree",
        action='store_const',
        const=True,
        default=False,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--disposition",
        action='store_const',
        const=True,
        default=False,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--simplify",
        "--no-simplify",
        dest="simplify",
        default=True,
        action=NegateAction,
        nargs=0,
        help="simplify some structures into more human readable forms"
    )

    parser.add_argument(
        "--hide-unneeded",
        "--no-hide-unneeded",
        dest="hide_unneeded",
        default=True,
        action=NegateAction,
        nargs=0,
        help="hide unneeded info (e.g. array element counts)",
    )

    parser.add_argument(
        "--resolve",
        "--no-resolve",
        dest="resolve",
        default=True,
        action=NegateAction,
        nargs=0,
        help="resolve fileids when possible (requires listfile)",
    )

    parser.add_argument(
        "--listfile",
        default=os.path.join(DATADIR, "listfile.csv"),
        help="specify listfile to use for fileids (default: %(default)s)",
    )

    parser.add_argument(
        "--filter",
        dest="filters",
        default=[],
        action='append',
        nargs=1,
        help="filter results by path (can be used multiple times)",
    )

    # These next two aren't intended to be used by the user, just to make
    # our lives easier later. There's probably a better way.
    parser.add_argument(
        "--filters_keep",
        default=[],
        nargs="*",
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--filters_discard",
        default=[],
        nargs="*",
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--precision",
        action='store',
        type=int,
        default=6,
        help="decimal digits to include on simplified floats",
    )

    parser.add_argument(
        "--arraylimit",
        action='store',
        type=int,
        default=25,
        help="elide array contents after this many entries (0 disables elision)",
    )

    # FIXME: Not sure this is the best way to handle this?
    parser.add_argument(
        "--geometry",
        "--no-geometry",
        dest="geometry",
        default=False,
        action=NegateAction,
        nargs=0,

        help="Decode individual vertexes and related fields"
    )

    parser.add_argument(
        "--elide-all",
        action='store_true',
        default=False,
        help="Limit array size on all fields, not just geometry-related",
    )

    parser.add_argument(
        "--bulk-overwrite",
        action='store_true',
        default=False,
        help="Allow 'bulkwalk' to overwrite existing output files,"
    )

    # FIXME: Allow multiple types
    parser.add_argument(
        "--bulk-type",
        action='store',
        type=str,
        default=None,
        help="Limit bulkwalk to processing only this type",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,

        help="file to output results to",
    )

    parser.add_argument(
        "file",
        action='store',
        # nargs='+',
        # default=[],
        help="input file to be processed",
    )

    args = parser.parse_args(argv)

    if args.debug:
        args.log_level = 'DEBUG'

    # args.filters = [item for subl in args.filters for item in subl]
    # prep our filters
    for filter in [item for subl in args.filters for item in subl]:
        # args.arraylimit = 0  # can't have an array limit when filtering right now
        if filter.startswith("!"):
            args.filters_discard.append(filter.lstrip("!"))
        else:
            args.filters_keep.append(filter)

    return args


def fileparse(file):
    # FIXME: commented out code is previous error handling, figure out if
    # we need that still, and how, and where
    # try:
    #     target = load_wowfile(file)
    # except (ValueError, OSError) as e:
    #     print(f"ERROR: {e}", file=sys.stderr)
    #     return 65  # os.EX_DATAERR
    return filetypes.load_wowfile(file)


def walk_file(args, infile: pathlib.Path, outfile: pathlib.Path, overwrite: bool, cachecon):
    logger = logging.getLogger("pathwalk")

    if not overwrite and outfile.exists():
        logger.debug(f"skipping due to existing output file: {infile}")
        return

    outfile.parent.mkdir(parents=True, exist_ok=True)

    logger.debug(f"processing input file: {infile}")
    if args.verbose:
        print(f"processing: {infile}", file=sys.stderr)

    target = fileparse(infile)
    with DataOutput(outfile) as out:
        if not check_filtered("/contenthash"):
            h = get_contenthash(infile)
            out.write(f"/contenthash = {h}")

        for line in pathwalk(target, "", cachecon):
            out.write(line)


def cmd_pathwalk(args):
    # FIXME: better error handling (or error handling at all)
    cachecon = cache_prepare(args)
    with DataOutput(args.output) as out:
        target = fileparse(args.file)

        # out.write(f"# path = {file}")
        if not check_filtered("/contenthash"):
            h = get_contenthash(args.file)
            out.write(f"/contenthash = {h}")

        for line in pathwalk(target, "", cachecon):
            out.write(line)

    return 0


# FIXME: How do we deal with errors and such?
def cmd_bulkwalk(args):
    logger = logging.getLogger("bulkwalk")

    if not args.output:
        print("ERROR: bulkwalk requires --output be specified", file=sys.stderr)
        return 64  # os.EX_USAGE

    # FIXME: Should we just create it if it doesn't exist?
    outdir = pathlib.Path(args.output)
    if not outdir.exists() or not outdir.is_dir():
        print(f"ERROR: doesn't exist or isn't a directory: {outdir}")
        return 65  # os.EX_DATAERR

    indir = pathlib.Path(args.file)
    if not indir.exists() or not indir.is_dir():
        print(f"ERROR: doesn't exist or isn't a directory: {indir}")
        return 65  # os.EX_DATAERR

    cachecon = cache_prepare(args)
    supported = filetypes.get_supported()

    for dirpath, _dirs, files in os.walk(indir):
        for file in files:
            inpath = indir / file
            ext = inpath.suffix.lower()
            if ext not in supported:
                logger.debug(f"skipping file with unknown type: {inpath}")
                continue

            if args.bulk_type and f".{args.bulk_type}" != ext:
                logger.debug(f"skipping file with non-requested type: {inpath}")
                continue

            # supported/requested filetype, so process it
            inpath = pathlib.Path(dirpath) / file

            out_file = inpath.name + ".txt"
            outsubpath = pathlib.Path(*inpath.parts[1:])  # drop the first bit
            outpath = outdir / outsubpath.parent / out_file

            # Ugh, finally done with path juggling, maybe we can actually,
            # y'know, process something?
            try:
                walk_file(args, inpath, outpath, args.bulk_overwrite, cachecon)
            except (OSError, EOFError, KaitaiStructError) as e:
                logger.warning(f"error while processing: {e}")
                outpath.unlink(missing_ok=True)

    return 0


def cmd_raw(args):
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        out.write(ppretty(target, depth=99, seq_length=100,))

    return 0


def cmd_final(args):
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        parsed = kttree(target)
        out.write(ppretty(parsed, depth=99, seq_length=100,))

    return 0


def cmd_json(args):
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        parsed = kttree(target)
        out.write(json.dumps(parsed, indent=2, sort_keys=True))

    return 0


# FIXME: Make argparse pull from here
cmds = {
    "pathwalk": cmd_pathwalk,
    "bulkwalk": cmd_bulkwalk,
    "raw": cmd_raw,
    "final": cmd_final,
    "json": cmd_json,
}


def main(argv=None):
    # arg parsing
    global args
    if not argv:
        argv = sys.argv[1:]

    LOGGER_LIST = ["disposition", "simplify", "kttree"]
    args = parse_arguments(argv, loggers=LOGGER_LIST)


    # Logging setup
    LOG_FORMAT = "[%(filename)s:%(lineno)s:%(funcName)s] (%(name)s) %(levelname)s: %(message)s"
    logging.basicConfig(level=args.log_level, format=LOG_FORMAT)

    for lg in LOGGER_LIST:
        if getattr(args, f"debug_{lg}"):
            x = logging.getLogger(lg)
            x.setLevel(logging.DEBUG)


    # Actual commands
    if args.mode in cmds:
        # FIXME: should we just be using exceptions for all our exit paths?
        return cmds[args.mode](args)
    else:
        print(f"ERROR: unknown mode {args.mode} (this shouldn't happen)")
        return 70  # os.EX_SOFTWARE

    return 0  # os.EX_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
