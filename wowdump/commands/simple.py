# these are really straightforward commands, with almost no code,
# so really don't need their own individual files
import argparse
import json

from ppretty import ppretty

from .. import reports
from ..dumputil import DataOutput, fileparse, kttree


def cmd_raw(args: argparse.Namespace) -> int:
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        out.write(ppretty(target, depth=99, seq_length=100,))

    return 0


def cmd_final(args: argparse.Namespace) -> int:
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        parsed = kttree(target)
        out.write(ppretty(parsed, depth=99, seq_length=100,))

    return 0


def cmd_json(args: argparse.Namespace) -> int:
    with DataOutput(args.output) as out:
        target = fileparse(args.file)
        parsed = kttree(target)
        out.write(json.dumps(parsed, indent=2, sort_keys=True))

    return 0


def cmd_report(args: argparse.Namespace) -> int:
    with DataOutput(args.output) as out:
        # FIXME: Why does mypy think 'reports' doesn't have a 'wmo'?
        reports.wmo(args, args.file, out)

    return 0
