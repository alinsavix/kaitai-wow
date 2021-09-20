#!/usr/local/bin/python3
import argparse
import csv
import hashlib
import inspect
import json
import os
import re
import sys
import time
from typing import Any, Callable, Dict, List, Optional, Union, TextIO

import logging
from kaitaistruct import BytesIO, KaitaiStream, KaitaiStruct
from ppretty import ppretty

from .dumputil import kttree
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
    fileHandle: TextIO
    is_stdout: bool

    def __init__(self, fn: Optional[str]):
        if fn is not None:
            self.fileHandle = open(fn, "w")
            self.is_stdout = False
        else:
            self.fileHandle = sys.stdout
            self.is_stdout = True

    def close(self):
        # only close if not stdout
        if not self.is_stdout:
            self.fileHandle.close()

    def write(self, outstr: str):
        print(outstr, file=self.fileHandle, flush=self.is_stdout)


import contextlib
@contextlib.contextmanager
def dataout(fn: Optional[str]):
    output = DataOutput(fn)
    yield output
    output.close()


# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_TARGET = "testfiles/staff_2h_draenorcrafted_d_02_c.m2"
CASCDIR = None
DATADIR = os.path.dirname(os.path.realpath(__file__))

# FIXME: Turn these into proper verbosity flags
do_verbose = 0
do_debug = 0
showtree = 0
do_disposition = 0

global args

def log(text):
    if do_verbose:
        # print(text, file=sys.stderr)
        print(text, flush=True)


def debug(text):
    if do_debug:
        # print(text, file=sys.stderr)
        print("DEBUG", text, flush=True)


def disp(path, what):
    if do_disposition:
        print(f":: {path} --> {what}", flush=True)


def treepath(path, key, value=None):
    # log(f"treepath: {path}.{key} ({value})")
    if not value:
        # if key == "data":
        #     return path

        # else
        return f"{path}.{key}"

    # else
    if showtree:
        print(f"{path}.{key} == {value}", flush=True)


def pathpath(path, key):
    return f"{path}/{key}"


def whatis(obj):
    objis = []

    if inspect.ismodule(obj):
        objis.append("module")
    if inspect.isclass(obj):
        objis.append("class")
    if inspect.ismethod(obj):
        objis.append("method")
    if inspect.isfunction(obj):
        objis.append("function")
    if inspect.isgeneratorfunction(obj):
        objis.append("generatorfunction")
    if inspect.isgenerator(obj):
        objis.append("generator")
    if inspect.iscoroutinefunction(obj):
        objis.append("coroutinefunction")
    if inspect.iscoroutine(obj):
        objis.append("coroutine")
    if inspect.isawaitable(obj):
        objis.append("awaitable")
    if inspect.isasyncgenfunction(obj):
        objis.append("asyncgenfunction")
    if inspect.isasyncgen(obj):
        objis.append("asyncgen")
    if inspect.istraceback(obj):
        objis.append("traceback")
    if inspect.isframe(obj):
        objis.append("frame")
    if inspect.iscode(obj):
        objis.append("code")
    if inspect.isbuiltin(obj):
        objis.append("builtin")
    if inspect.isroutine(obj):
        objis.append("routine")
    if inspect.isabstract(obj):
        objis.append("abstract")
    if inspect.ismethoddescriptor(obj):
        objis.append("methoddescriptor")
    if inspect.isdatadescriptor(obj):
        objis.append("datadescriptor")
    if inspect.isgetsetdescriptor(obj):
        objis.append("getsetdescriptor")
    if inspect.ismemberdescriptor(obj):
        objis.append("memberdescriptor")

    if isinstance(obj, KaitaiStruct):
        objis.append("kaitaistruct")

    return objis


def get_contenthash(filename):
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
def find_related(filepath, base):
    if os.path.isfile(base):
        base = os.path.dirname(base)

    filename = os.path.basename(filepath)
    check = os.path.join(base, filename)
    if os.path.isfile(check):
        return check

    if CASCDIR:
        check = os.path.join(CASCDIR, filepath)
        if os.path.isfile(check):
            return check

    return None


# "kaitai type"
def ktype(v):
    logger = logging.getLogger()
    if inspect.isclass(v):
        logger.debug("var is type class, skipping")
        return "skip"

    if inspect.ismethod(v) or inspect.isbuiltin(v):
        logger.debug("var is is method or builtin, skipping")
        return "skip"

    if isinstance(v, type):
        logger.debug("var is defines a datatype, skipping")
        return "skip"

    if isinstance(v, list):
        logger.debug("var is type list")
        return "list"

    if isinstance(v, KaitaiStruct):
        logger.debug(f"var is a kaitai type {type(v)}")
        return "kaitai"

    if type(v) in [int, float, str, bool]:
        logger.debug("var is a base type")
        return "base"

    # otherwise is a dict type
    # FIXME: I think dict type, anyhow
    logger.debug("var is (probably) a dict type")
    return "dict"


# FIXME: needs dict key sorting (if possible)
def walk(out: DataOutput, obj, path: str, cachecon) -> None:
    lgsimplify = logging.getLogger("simplify")
    lgdisp = logging.getLogger("disposition")

    logger = logging.getLogger()
    logger.debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    # This is kind of a lame way to get a loop that handles both lists
    # and dicts, but is there a better way?
    if isinstance(obj, dict):
        logger.debug(f"using sorted dict for {path}")
        obj_keys = sorted(dir(obj), key=lambda x: (
            not (x == "chunk_size" or x == "chunk_type"), x))

    # FIXME: isn't detecting ... /model/vertices
    elif isinstance(obj, list):
        logger.debug(f"using list for {path}")
        obj_keys = range(0, len(obj))
    else:
        logger.debug(f"using normal ordering for {path}")
        obj_keys = dir(obj)

    # if path == "/skin/batches/0":
    #     print("breakpoint")

    eject = False
    for k in obj_keys:
        # Is this right? Do we want to return completely if we're ejecting?
        if eject:
            return

        if k[0] == "_":
            continue

        workpath = f"{path}/{k}"

        # if workpath == "/model/vertices":
        #     print("breakpoint")


        # FIXME: figure out what to do with m2track
        # if k == "m2array_type" or k == "m2track_type":
        #     lgdisp.debug(f"{workpath} --> ignored")
        #     continue
        if k == "m2array_type":
            lgdisp.debug(f"{workpath} --> ignored")
            continue

        logger.debug(f"getattr {k} from obj type {type(obj)}")
        v = getattr(obj, k)

        kt = ktype(v)
        if kt == "skip":  # class, method, datatype
            continue

        # if workpath == "/model/vertices":
        #     print("breakpoint")

        logger.debug(f"checking for array elision for {workpath}")
        # this is probably a code smell, if not worse. If our current level
        # isn't geometry, but we add a '/0' to it and it is, that means it's
        # the very top of a geometry tree, and we can save ourselves the
        # effort of descending into it (and thus reading & parsing it) by
        # just escaping now.
        if not args.geometry and not geometry_path(workpath) and geometry_path(f"{workpath}/0"):
            # seriously, fuuuuuuugly
            out.write(
                f"{workpath}/... = [geometry data elided, use --geometry to include]")
            continue

        if geometry_path(workpath) and args.arraylimit > 0 and k >= args.arraylimit:
            logger.debug(f"eliding remaining geometry entries for {workpath}")
            remaining = len(d) - args.arraylimit
            out.write(
                f"{path}/... = [{remaining-1} elided of {len(obj)} total]")
            k = obj_keys[-1]
            eject = True
            continue

        if args.elide_all and isinstance(obj, list) and args.arraylimit > 0 and k >= args.arraylimit:
            logger.debug(f"eliding remaining array entries for {workpath}")
            remaining = len(d) - args.arraylimit
            out.write(
                f"{path}/... = [{remaining-1} elided of {len(obj)} total]")
            k = obj_keys[-1]
            eject = True
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

            # FIXME: this feels sloppy
            if kt == "base" or kt == "list":
                simplified = s(v, obj, cachecon, args)
            else:
                simplified = s(v, obj, cachecon, args)
            if simplified is not None:
                out.write(f"{workpath} = {simplified}")

            # We either simplified w/ output, or simplified out of existence.
            # either way, move on
            continue

        if kt == "list":
            lgdisp.debug(f"{workpath}[] --> array processing (len {len(v)})")

            for i, el in enumerate(v):
                arraypath = f"{workpath}/{i}"
                elt = ktype(el)

                # FIXME: dedupe dedupe
                s = check_simplify(arraypath) if args.simplify else None

                if s:
                    lgsimplify.debug(f"using simplifier for {arraypath}")

                    lgsimplify.debug(
                        f"array simplify type: {type(el)}   value: {el}")
                    # FIXME: this feels sloppy
                    if elt == "base" or elt == "list":
                        simplified = s(el, v, cachecon, args)
                    else:
                        simplified = s(el, v, cachecon, args)
                    if simplified is not None:
                        out.write(f"{arraypath} = {simplified}")

                    # We either simplified w/ output, or simplified out of existence.
                    # either way, move on
                    continue

                # if elt in [int, float, str]:
                if elt == "base":
                    if isinstance(el, str):
                        el = el.rstrip("\0")
                    lgdisp.debug(f"array {arraypath} --> final ({el})")
                    out.write(f"{arraypath} = {el}")

                    # print thing?
                    # value.append(el)
                else:
                    lgdisp.debug(f"{arraypath} --> array descent")
                    # value.append(to_tree(el, treepath(path, k + f"[{i}]")))
                    walk(out, el, arraypath, cachecon)

        elif kt == "kaitai":
            # FIXME: I think we're supposed to do one of these without the {k}
            if k == "data":
                lgdisp.debug(f"{workpath} --> kaitai data descent")
                walk(out, v, workpath, cachecon)
            else:
                lgdisp.debug(f"{workpath} --> kaitai descent type {type(k)}")
                # debug(f"recursing kaitai value, type: {type(k)}")
                walk(out, v, workpath, cachecon)

        elif kt == "base":
            if isinstance(v, str):
                v = v.rstrip("\0")
            lgdisp.debug(f"{workpath} --> final ({v})")
            # logger.debug(f"(output) {v}")
            out.write(f"{workpath} = {v}")

        else:
            lgdisp.debug(f"{workpath} --> descend (type {type(v)}")
            walk(out, v, workpath, cachecon)

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
def cache_open(dbfile: str):
    if "sqlite3" not in sys.modules:
        print("WARNING: sqlite not available, caching disabled", file=sys.stderr)
        return None

    # FIXME: can we do better than a global variable?
    cachecon = sqlite3.connect(dbfile)

    return cachecon


def cache_fileids(listfile: str, cachecon) -> None:
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

# FIXME: Can we manage the cache better than jut passing cachecon around?
def pathdump(out: DataOutput, d, path: str, cachecon) -> None:
    # This is kind of a lame way to get a loop that handles both lists
    # and dicts, but is there a better way?
    if isinstance(d, dict):
        things = sorted(d.keys(), key=lambda x: (
            not (x == "chunk_size" or x == "chunk_type"), x))
    elif isinstance(d, list):
        things = range(0, len(d))

    eject = False
    for k in things:
        if eject:
            return

        if isinstance(d, list) and (args.elide_all or geometry_path(f"{path}/{k}")) \
                and args.arraylimit > 0 and k >= args.arraylimit:
            remaining = len(d) - args.arraylimit
            out.write(f"{path}/... = [{remaining-1} elided of {len(d)} total]")
            k = things[-1]
            eject = True
            # return

        workpath = f"{path}/{k}"
        thing = d[k]

        # if we have ofs_xxx or num_xxx, and *also* just have xxx,
        # we don't need the offset/size anymore
        if args.hide_unneeded and isinstance(k, str) and (k.startswith("ofs_") or k.startswith("num_")):
            s = k[len("ofs_"):]
            if s in things:
                continue

        # if check_filtered(workpath):
        #     continue

        # doublecheck to make sure check_simply doesn't get called if disabled
        s = check_simplify(workpath) if args.simplify else None

        if s:
            # if it's simplified, we're at a 'final' path, so check filtering
            if check_filtered(workpath):
                continue
            simplified = s(thing, d, cachecon, args)
            if simplified is not None:
                out.write(f"{workpath} = {simplified}")
        elif isinstance(thing, dict) or isinstance(thing, list):
            pathdump(out, thing, workpath, cachecon)
        else:
            # we're at a final path, so check filtering
            if check_filtered(workpath):
                continue

            # FIXME: Not sure if this is a kaitai bug or what, but we're
            # getting nulls at the end of strings right now. This cleans
            # that up for now.
            if isinstance(thing, str):
                thing = thing.rstrip("\0")
            out.write(f"{workpath} = {thing}")

    return


class NegateAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'no')

def parse_arguments(argv, loggers):
    parser = argparse.ArgumentParser(
        prog="wowdump",
        description="A tool for dumping the information out of WoW files",
    )

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
            #help = "whatever",
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
        default=f"{DATADIR}/listfile.csv",
        help="specify listfile to use for fileids (default: %(default)s",
    )

    parser.add_argument(
        "--filter",
        dest="filters",
        default=[],
        action='append',
        nargs="+",
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
        "--output_type",
        "--output-type",
        "-t",
        choices=["path", "json", "final", "raw", "walk", ],
        default="walk",
        help="select output type (default: %(default)s)",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,

        help="file to output results to",
    )

    parser.add_argument(
        "files",
        action='store',
        nargs='+',
        default=[],
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


def main(argv=None):
    global args
    if not argv:
        argv = sys.argv[1:]

    LOGGER_LIST = ["disposition", "simplify", "kttree"]
    args = parse_arguments(argv, loggers=LOGGER_LIST)

    LOG_FORMAT = "[%(filename)s:%(lineno)s:%(funcName)s] (%(name)s) %(levelname)s: %(message)s"
    logging.basicConfig(level=args.log_level, format=LOG_FORMAT)

    for lg in LOGGER_LIST:
        if getattr(args, f"debug_{lg}"):
            l = logging.getLogger(lg)
            l.setLevel(logging.DEBUG)

    log = logging.getLogger()
    log.info("wowdump initialized")  # FIXME: remove me

    # if len(args.files) == 0:
    #     args.files = [DEFAULT_TARGET]
    #     print(
    #         f"WARNING: Using default target file {DEFAULT_TARGET}", flush=True, file=sys.stderr)

    if not args.resolve:
        # print("INFO: not resolving, not initializing cache", file=sys.stderr)
        cachecon = None
    elif not os.path.exists(args.listfile):
        log.warning(
            f"{args.listfile} does not exist, not resolving fileids")
        cachecon = None
    else:
        cachefile = f"{args.listfile}.cache"
        if os.path.exists(cachefile) and (os.path.getmtime(args.listfile) <= os.path.getmtime(cachefile)):
            # print("INFO: fileid cache up to date, not updating", file=sys.stderr)
            cachecon = cache_open(cachefile)
        else:
            cachecon = cache_open(cachefile)
            cache_fileids(args.listfile, cachecon)

    # FIXME: handle more than one file
    file = args.files[0]

    if not os.path.isfile(file):
        log.error(f"no such file: {file}")
        return 1

    name, ext = os.path.splitext(file)
    if ext == ".m2":
        from .filetypes.m2 import M2
        target = M2.from_file(file)
    elif ext == ".skin":
        from .filetypes.skin import Skin
        target = Skin.from_file(file)
    elif ext == ".skel":
        from .filetypes.skel import Skel
        target = Skel.from_file(file)
    elif ext == ".blp":
        from .filetypes.blp import Blp
        target = Blp.from_file(file)
    elif ext == ".bls":
        from .filetypes.bls import Bls
        target = Bls.from_file(file)
    elif ext == ".wmo":
        from .filetypes.wmo import Wmo
        target = Wmo.from_file(file)
    elif ext == ".wdt":
        from .filetypes.wdt import Wdt
        target = Wdt.from_file(file)
    elif ext == ".anim":
        from .filetypes.anim import Anim
        target = Anim.from_file(file)
    else:
        print(
            f"ERROR: don't know how to parse file type {ext}", file=sys.stderr)
        sys.exit(1)

    with dataout(args.output) as out:
        if args.output_type == "path":
            parsed = kttree(target)
            # out.write(f"# path = {file}")
            h = get_contenthash(file)
            out.write(f"# contenthash = {h}")

            pathdump(out, parsed, "", cachecon)
        elif args.output_type == "raw":
            out.write(ppretty(target, depth=99, seq_length=100,))
        elif args.output_type == "final":
            parsed = kttree(target)
            out.write(ppretty(parsed, depth=99, seq_length=100,))
        # FIXME: re-enable json, make it use out.write()
        elif args.output_type == "json":
            parsed = kttree(target)
            json.dump(parsed, fp=sys.stdout, indent=2, sort_keys=True)
            print()  # newline at end
        elif args.output_type == "walk":
            # out.write(f"# path = {file}")
            h = get_contenthash(file)
            out.write(f"# contenthash = {h}")

            # temporary for performance work
            walk(out, target, "", cachecon)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
