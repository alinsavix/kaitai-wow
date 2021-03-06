import argparse
from pathlib import Path

from ..dumputil import DataOutput, fileparse, get_contenthash
from ..filters import check_filtered
from ..pathwalk import pathwalk


def cmd_pathwalk(args: argparse.Namespace) -> int:
    # FIXME: better error handling (or error handling at all)
    # FIXME: bundle filetype into args?
    filetype = Path(args.file).suffix.lstrip('.')
    with DataOutput(args.output) as out:
        target = fileparse(args.file)

        # out.write(f"# path = {file}")
        if not check_filtered(args, "/contenthash"):
            h = get_contenthash(args.file)
            out.write(f"/contenthash = {h}")

        for line in pathwalk(args, target, "", filetype):
            out.write(line)

    return 0
