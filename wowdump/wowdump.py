import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Text, Union

import requests

from . import csvcache
from .commands import (WowdumpCommand, cmd_bulkwalk, cmd_final, cmd_json,
                       cmd_pathwalk, cmd_raw, cmd_report)

# from ppretty import ppretty

# This script is what's known as "awful". It's brute force. It does
# everything wrong. It probably doesn't even taste like chocolate.
# But should at least give a baseline for dumping interesting info
# out of interesting files, even if it *is* garbage at the moment.
#
# Also, did I mention it's garbage?


# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_LISTFILE: str = str(Path.home() / ".wowdump_listfile.csv")
DEFAULT_LISTFILE_URL: str = "https://wow.tools/casc/listfile/download/csv/unverified"
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
def get_default_listfile() -> str:
    return DEFAULT_LISTFILE

def set_default_listfile(listfile: str) -> None:
    global DEFAULT_LISTFILE
    DEFAULT_LISTFILE = listfile

def download_listfile(dest: Union[str, os.PathLike[str]], url: str) -> None:
    logger = logging.getLogger()

    dest = Path(dest)
    tmpfile = dest.with_suffix(".tmp")

    if dest.exists() and not dest.is_file():
        raise ValueError(f"{dest} exists but isn't a file")

    # for whatever reason, cloudflare blocks this if it's just the normal
    # python 'requests' user agent
    headers = {
        'User-Agent': 'wowdump/1.0',
    }

    print(f"NOTICE: downloading new listfile to {args.listfile}", file=sys.stderr)
    logger.debug("requesting new listfile from {url}")

    # FIXME: How in the bloody fuck do you get a useful human-readable
    # error message out of the requests library? e.g. trying to go to an
    # invalid hostname will return a generic "ConnectionError" error, even
    # though more specific data is available. The full exception thrown is:
    #
    # HTTPConnectionPool(host='asdf', port=80): Max retries exceeded with
    # url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection
    # object at 0x1085c4a60>: Failed to establish a new connection: [Errno 8]
    # nodename nor servname provided, or not known'))
    #
    # it would be really great to be able to provide "nodename nor servname
    # provided, or not known" to the user, but best I can figure there's no
    # way to extract that information from the exception short of string
    # matching. Ugh. Tempted to just use urllib directly.
    with tmpfile.open(mode="wb") as outfile:
        try:
            r = requests.get(url, stream=True, headers=headers)
        except requests.exceptions.HTTPError as e:
            raise ValueError(f"HTTP error: {e}")
        except requests.exceptions.ConnectionError as e:
            raise ValueError(f"connection error: {e}")
        except requests.exceptions.Timeout as e:
            raise ValueError(f"timeout error: {e}")
        except requests.exceptions.TooManyRedirects as e:
            raise ValueError(f"too many redirects: {e}")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"unknown error: {e}")

        if r.status_code != 200:
            raise ValueError(
                f"couldn't download listfile: {r.status_code} {r.reason} (url: {url})")
        outfile.write(r.content)

    tmpfile.replace(dest)


class NegateAction(argparse.Action):
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace,
                 values: Union[Text, Sequence[Any], None], option_string: Optional[Text] = "") -> None:
        assert option_string is not None  # n
        setattr(namespace, self.dest, option_string[2:4] != 'no')


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
        # default=Path.home() / ".wowdump_listfile.csv",
        type=str,
        default=None,
        help=f"specify listfile to use for fileids (default: {DEFAULT_LISTFILE})",
    )

    parser.add_argument(
        "--listfile-url",
        type=str,
        default=DEFAULT_LISTFILE_URL,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--download-listfile",
        "--no-download-listfile",
        dest="download_listfile",
        default=None,
        action=NegateAction,
        nargs=0,
        help="download/suppress downloading of a new listfile from wow.tools",
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
        nargs='?',
        default=None,
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


# FIXME: Make argparse pull from here
cmds: Dict[str, WowdumpCommand] = {
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
    # if not argv:
    #     argv = sys.argv[1:]

    LOGGER_LIST = ["disposition", "simplify", "kttree", "csvcache"]
    args = parse_arguments(argv, loggers=LOGGER_LIST)

    # Logging setup
    LOG_FORMAT = "[%(filename)s:%(lineno)s:%(funcName)s] (%(name)s) %(levelname)s: %(message)s"
    logging.basicConfig(level=args.log_level, format=LOG_FORMAT)

    for lg in LOGGER_LIST:
        if getattr(args, f"debug_{lg}") or os.getenv(f"DEBUG_{lg}") is not None:
            x = logging.getLogger(lg)
            x.setLevel(logging.DEBUG)

    if args.listfile is None:
        args.listfile = DEFAULT_LISTFILE

    if not os.path.exists(args.listfile) and args.listfile == DEFAULT_LISTFILE:
        if args.download_listfile is None:
            print("WARNING: listfile does not exist, a new listfile will be downloaded", file=sys.stderr)
            args.download_listfile = True
        elif args.download_listfile is False:
            print("WARNING: listfile does not exist, fdid name resolution disabled", file=sys.stderr)
            args.download_listfile = False
            args.resolve = False

    if args.download_listfile:
        try:
            download_listfile(args.listfile, args.listfile_url)
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 69  # os.EX_UNAVAILABLE

    if args.resolve:
        csvcache.init("listfile", args.listfile)
    else:
        csvcache.init("listfile", None)

    if args.file is None:
        return 0

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
