import argparse
import logging
import os
import sys
from typing import Callable, Dict, List, Optional

from .commands import (cmd_bulkwalk, cmd_final, cmd_json, cmd_pathwalk,
                       cmd_raw, cmd_report)

# from ppretty import ppretty



# This script is what's known as "awful". It's brute force. It does
# everything wrong. It probably doesn't even taste like chocolate.
# But should at least give a baseline for dumping interesting info
# out of interesting files, even if it *is* garbage at the moment.
#
# Also, did I mention it's garbage?


# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_TARGET = "testfiles/staff_2h_draenorcrafted_d_02_c.m2"
CASCDIR = None
DATADIR = os.path.dirname(os.path.realpath(__file__))

args: argparse.Namespace

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


class NegateAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'no')

def parse_arguments(argv: List[str], loggers: List[str]) -> argparse.Namespace:
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

    cmdgroup.add_argument(
        '--report',
        action='store_const',
        const="report",
        dest="mode",
        help="human-readable simplified file report"
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

    # FIXME: The way we handle logger configs sucks
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


WowddumpCommand = Callable[[argparse.Namespace], int]
# FIXME: Make argparse pull from here
cmds: Dict[str, WowddumpCommand] = {
    "pathwalk": cmd_pathwalk,
    "bulkwalk": cmd_bulkwalk,
    "raw": cmd_raw,
    "final": cmd_final,
    "json": cmd_json,
    "report": cmd_report,
}


def main(argv: Optional[List[str]] = None) -> int:
    # arg parsing
    global args
    if not argv:
        argv = sys.argv[1:]

    LOGGER_LIST = ["disposition", "simplify", "kttree", "csvcache"]
    args = parse_arguments(argv, loggers=LOGGER_LIST)

    # Logging setup
    LOG_FORMAT = "[%(filename)s:%(lineno)s:%(funcName)s] (%(name)s) %(levelname)s: %(message)s"
    logging.basicConfig(level=args.log_level, format=LOG_FORMAT)

    for lg in LOGGER_LIST:
        if getattr(args, f"debug_{lg}") or os.getenv(f"DEBUG_{lg}") is not None:
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
