#!/usr/local/bin/python3
import argparse
import csv
import json
import hashlib
import os
import re
import sys
import time
from typing import Any, Optional, Dict, List, Callable
from ppretty import ppretty
import inspect

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

# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_TARGET = "testfiles/staff_2h_draenorcrafted_d_02_c.m2"
#CASCDIR = None
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


def to_tree(obj, path: str = ""):
    r = {}
    debug(f"in: path: {path}  type: {type(obj)} {whatis(obj)}")

    value = None

    for k in dir(obj):
        if k[0] == "_":
            continue

        debug(f"getattr {k} from obj type {type(obj)}")
        v = getattr(obj, k)
        # t = type(v)
        # debug(f"processing attribute {k} type {t}")
        # if inspect.isclass(v) or inspect.ismethod(v):

        if inspect.isclass(v):
            # debug(f"is class, skipping")
            pass
        elif inspect.ismethod(v) or inspect.isbuiltin(v):
            # debug(f"is method or builtin, skipping")
            pass
        elif isinstance(v, type):
            # debug(f"defines a datatype, skipping")
            pass
        else:
            if type(v) == type([]):
                # if isinstance(v, list):
                # debug("processing array type")
                # log(f"array is: {ppretty(v)}")
                disp(f"{path}.{k}[]", f"array processing (len {len(v)})")
                value = []
                for i, el in enumerate(v):
                    # debug(f"appending {el}")
                    if type(el) in [int, float, str]:
                        disp(f"{path}[{i}]", f"final ({el})")
                        value.append(el)
                    else:
                        disp(f"{path}[{i}]", "array descent")
                        value.append(to_tree(el, treepath(path, k + f"[{i}]")))
            elif isinstance(v, KaitaiStruct):
                if k == "data":
                    disp(f"{path}", "kaitai data descent")
                    value = to_tree(v, treepath(path, k))
                else:
                    disp(f"{path}.{k}", "kaitai descent")
                    # debug(f"recursing kaitai value, type: {type(k)}")
                    value = to_tree(v, treepath(path, k))
            else:
                # log(f"using plain value: {v} {whatis(v)}")
                # debug(f"dir: {dir(v)}")
                # print(ppretty(v))

                # treepath(path, k, v)
                # print(f"{path}.{k} == {v}")
                # value = v
                # value = to_tree(v, treepath(path, k))
                if type(v) in [int, float, str, bool]:
                    disp(f"{path}.{k}", f"final ({v})")
                    value = v
                else:
                    if k == "m2array_type" or k == "m2track_type":
                        disp(f"{path}.{k}", "ignored")
                    else:
                        disp(f"{path}.{k}", f"descend (type {type(v)}")
                        value = to_tree(v, treepath(path, k))

            if value is not None:
                r[k] = value

    debug(f"out:  returning {r}")
    return r


# Caching bits (yeah, they're ugly)
# or maybe type of os.PathLike for cache_open
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


def cache_getfileid(id: int, cachecon) -> Optional[str]:
    if not cachecon:
        return None

    cur = cachecon.cursor()
    q = "SELECT name FROM file_ids WHERE id=?"

    try:
        res = cur.execute(q, [id]).fetchone()
    except sqlite3.Error as e:
        print(f"ERROR: Unexpected sqlite error: {e}", file=sys.stderr)
        return False

    # not in cache? Return false so that we know not to try to fall back to
    # the listfile, since the cache should be authoritative
    if res is None:
        return False

    return res[0]


def csv_getfileid(id: int):
    try:
        with open("listfile.csv", 'r', newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                if int(row[0]) == id:
                    return f"{id}  # {row[1]}"
    except:
        pass

    return False


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
            # print(f"check filter {filter} vs {path}")
            if path.startswith(filter):
                return False

    if len(args.filters_discard):
        for filter in args.filters_discard:
            if path.startswith(filter):
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


# These next bits are an attempt to simplify certain structures into
# a more human-readable form. This is ugly and stupid and needs to
# be hand-maintained. We might be able to do better with some additional
# metadata out of kaitai or such, but for now, this is a quick and dirty
# "but I want to be able to read this" solution. There's probably better
# bad ways to do it, and definitely better not-bad ways to do it, but
# this works. For now. Until it offends my sight just a little too much
# and gets torn out by the roots (just like my hair)   --A
attachment_pos_re = re.compile(r'''
    ^/model/attachments/\d+/position$
''', re.VERBOSE)

bone_pivot_re = re.compile(r'''
    ^/model/bones/\d+/pivot$
''', re.VERBOSE)

bone_rot_re = re.compile(r'''
    ^/model/bones/\d+/rotation/values/values/\d+/values/\d+$
''', re.VERBOSE)

bone_xlate_re = re.compile(r'''
    ^/model/bones/\d+/translation/values/values/\d+/values/\d+$
''', re.VERBOSE)

flags_re = re.compile(r'''
    /(global_)?flags$
''', re.VERBOSE)

bbox_re = re.compile(r'''
    /(bounding_box|collision_box)/(min|max)$
''', re.VERBOSE)

events_pos_re = re.compile(r'''
    ^/model/events/\d+/position$
''', re.VERBOSE)

emitter_rgb_re = re.compile(r'''
    ^/model/particle_emitters/\d+/old/p/colors/values/values/\d+$
''', re.VERBOSE)

emitter_rot_scale_xlate_re = re.compile(r'''
    ^/model/particle_emitters/\d+/old/p/(rot\d|scales|trans)$
''', re.VERBOSE)

emitter_sizes_re = re.compile(r'''
    ^/model/particle_emitters/\d+/old/p/sizes/values/values/\d+$
''', re.VERBOSE)

emitter_position_re = re.compile(r'''
    ^/model/particle_emitters/\d+/old/position$
''', re.VERBOSE)

ambient_rgba_re = re.compile(r'''
    ^/chunks/\d+/chunk_data/amb_color$
''', re.VERBOSE)

wmomat_rgba_re = re.compile(r'''
    ^/chunks/\d+/chunk_data/materials/\d+/(diff_color|sidn_color|frame_sidn_color)$
''', re.VERBOSE)

wmomat_vertex_rgba_re = re.compile(r'''
    /chunks/\d+/chunk_data/vertex_colors/\d+$
''', re.VERBOSE)

wmomat_header_rgba_re = re.compile(r'''
    /chunks/\d+/chunk_data/header_color_replacement$
''', re.VERBOSE)

seq_bbox_re = re.compile(r'''
    ^/model/sequences/\d+/bounds/extent/(min|max)$
''', re.VERBOSE)

verts_vec_re = re.compile(r'''
    ^/model/vertices/\d+/(normal|pos)$
''', re.VERBOSE)

verts_wmo_re = re.compile(r'''
    /chunks/\d+/chunk_data/(vertices|normals)/\d+$
''', re.VERBOSE)

verts_wmo_textcoords_re = re.compile(r'''
    /chunks/\d+/chunk_data/(tex_coords)/\d+$
''', re.VERBOSE)

verts_texcoords_re = re.compile(r'''
    ^/model/vertices/\d+/tex_coords/\d+$
''', re.VERBOSE)

# FIXME: Can we make these behave better straight out of kaitai?
nested_xy_re = re.compile(r'''
    ^/model/particle_emitters/\d+/multi_texture_param\d/\d+$
''', re.VERBOSE)

fileids_re = re.compile(r'''
    ^/chunks/\d+/chunk_data/([^/]+_)?file_data_ids/\d+$
''', re.VERBOSE)

fileid_re = re.compile(r'''
    /([^/]+_)?file_data_id$
''', re.VERBOSE)

# FIXME: try to combine with the above
mapfileid_re = re.compile(r'''
    ^/chunks/\d+/chunk_data/map_fileids/\d+/[^/]+_file_data_id$
''', re.VERBOSE)

version_re = re.compile(r'''
    ^/model/version$
''', re.VERBOSE)

interpolation_type_re = re.compile(r'''
    interpolation_type$
''', re.VERBOSE)

# simplify_4bone
fourbone_re = re.compile(r'''
    ^/model/vertices/\d+/(bone_indices|bone_weights)$
''', re.VERBOSE)

runtime_re = re.compile(r'''
    /runtime_data$
''', re.VERBOSE)

unused_re = re.compile(r'''
    unused\d*$
''', re.VERBOSE)

def simplify_remove(d, _):
    return None

def simplify_xyz(d, _) -> str:
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    z = round(d["z"], args.precision)
    return f"xyz({x}, {y}, {z})"

def simplify_wxyz(d, _) -> str:
    w = round(d["w"], args.precision)
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    z = round(d["z"], args.precision)
    return f"wxyz({w}, {x}, {y}, {z})"

def simplify_xy(d, _) -> str:
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    return f"xy({x}, {y})"

def simplify_nested_xy(d, _) -> str:
    x = d["x"]["value"]
    y = d["y"]["value"]
    return f"xy({x}, {y})"

def simplify_irgb(d, _) -> str:
    r = int(d["r"])
    g = int(d["g"])
    b = int(d["b"])

    return f"rgb({r}, {g}, {b})  # {r:02x}{g:02x}{b:02x}"

def simplify_irgba(d, _) -> str:
    r = int(d["r"])
    g = int(d["g"])
    b = int(d["b"])
    a = int(d["a"])

    return f"rgba({r}, {g}, {b}, {a})  # {r:02x}{g:02x}{b:02x}{a:02x}"

def simplify_fourbone(d, _) -> str:
    return f"[ {d[0]}, {d[1]}, {d[2]}, {d[3]} ]"


# FIXME: Should the output be inside { } or something?
def simplify_flags(d, _):
    if not isinstance(d, dict):
        return d

    flags = []
    for k, v in d.items():
        if v:
            flags.append(k)

    if len(flags) == 0:
        return "none"

    return ", ".join(flags)


interpolation_types = {
    0: "interpolate_const",
    1: "interpolate_linear",
    2: "interpolate_cubic_bezier_spline",
    3: "interpolate_cubic_hermite_spline",
}

def simplify_enum(d, _):
    return f"{d['value']}  # {d['name']}"


# FIXME: This gonna be slow until database or caching
def resolve_fileid(id: id, cachecon) -> str:
    if not args.resolve or id <= 0:
        return f"{id}"

    c = cache_getfileid(id, cachecon)

    # if None, cache is not usable, so try the old fashioned way
    if c is None:
        c = csv_getfileid(id)

    if c is False:
        return f"{id}  # unresolved"
    else:
        return f"{id}  # {c}"


simplifications = [
    (runtime_re, simplify_remove),
    (unused_re, simplify_remove),
    (attachment_pos_re, simplify_xyz),
    (bone_pivot_re, simplify_xyz),
    (bone_rot_re, simplify_wxyz),
    (bone_xlate_re, simplify_xyz),
    (flags_re, simplify_flags),
    (bbox_re, simplify_xyz),
    (events_pos_re, simplify_xyz),
    (nested_xy_re, simplify_nested_xy),
    (emitter_rgb_re, simplify_irgb),
    (emitter_rot_scale_xlate_re, simplify_xyz),
    (emitter_sizes_re, simplify_xy),
    (emitter_position_re, simplify_xyz),
    (seq_bbox_re, simplify_xyz),
    (verts_vec_re, simplify_xyz),
    (verts_wmo_re, simplify_xyz),
    (verts_wmo_textcoords_re, simplify_xy),
    (verts_texcoords_re, simplify_xy),
    (fileid_re, resolve_fileid),
    (fileids_re, resolve_fileid),
    (mapfileid_re, resolve_fileid),
    (interpolation_type_re, simplify_enum),
    (fourbone_re, simplify_fourbone),
    (version_re, simplify_enum),
    (ambient_rgba_re, simplify_irgba),
    (wmomat_rgba_re, simplify_irgba),
    (wmomat_vertex_rgba_re, simplify_irgba),
    (wmomat_header_rgba_re, simplify_irgba),
]

def check_simplify(path: str):
    if not args.simplify:
        return None

    for r in simplifications:
        if r[0].search(path):
            return r[1]

    return None


# FIXME: Can we manage the cache better than jut passing cachecon around?
def pathdump(d, path: str, cachecon) -> None:
    # This is kind of a lame way to get a loop that handles both lists
    # and dicts, but is there a better way?
    if isinstance(d, dict):
        things = sorted(d.keys(), key=lambda x: (not (x == "chunk_size" or x == "chunk_type"), x))
    elif isinstance(d, list):
        things = range(0, len(d))

    eject = False
    for k in things:
        if eject:
            return

        if isinstance(d, list) and args.arraylimit > 0 and k >= args.arraylimit:
            remaining = len(d) - args.arraylimit
            print(f"{path}/... = [{remaining-1} elided of {len(d)} total]")
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

        s = check_simplify(workpath)
        if s:
            # if it's simplified, we're at a 'final' path, so check filtering
            if check_filtered(workpath):
                continue
            simplified = s(thing, cachecon)
            if simplified is not None:
                print(f"{workpath} = {simplified}")
        elif isinstance(thing, dict) or isinstance(thing, list):
            pathdump(thing, workpath, cachecon)
        else:
            # we're at a final path, so check filtering
            if check_filtered(workpath):
                continue

            # FIXME: Not sure if this is a kaitai bug or what, but we're
            # getting nulls at the end of strings right now. This cleans
            # that up for now.
            if isinstance(thing, str):
                thing = thing.rstrip("\0")
            print(f"{workpath} = {thing}")

    return


class NegateAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != 'no')

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="wowdump",
        description="A tool for dumping the information out of WoW files",
    )

    parser.add_argument(
        "--verbose",
        action='store_const',
        const=True,
        default=False,
        # help="Read objects and prepare them for decimation",
    )

    parser.add_argument(
        "--debug",
        action='store_const',
        const=True,
        default=False,
        # help="Read objects and prepare them for decimation",
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
        "--hide-unneeded"
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
        help="filter results by path (can be used multiple times)"
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
        help="decimal digits to include on simplified floats"
    )

    parser.add_argument(
        "--arraylimit",
        action='store',
        type=int,
        default=25,
        help="elide array contents after this many entries (0 disables elision)",
    )

    parser.add_argument(
        "--output_type",
        "-t",
        choices=["path", "json", "final", "raw", ],
        default="path",
        help="select output type (default: %(default)s)",
    )

    parser.add_argument(
        "files",
        action='store',
        nargs='*',
        default=[],
        help="input file to be processed",
    )

    args = parser.parse_args()

    # args.filters = [item for subl in args.filters for item in subl]
    # prep our filters
    for filter in [item for subl in args.filters for item in subl]:
        if filter.startswith("!"):
            args.filters_discard.append(filter.lstrip("!"))
        else:
            args.filters_keep.append(filter)

    return args


if __name__ == "__main__":
    global args
    args = parse_arguments()

    if len(args.files) == 0:
        args.files = [DEFAULT_TARGET]
        print(
            f"WARNING: Using default target file {DEFAULT_TARGET}", flush=True, file=sys.stderr)

    cache_current = False
    cachefile = f"{args.listfile}.cache"

    # FIXME: This is a bit deeply nested for my tastes.
    if not args.resolve:
        print("INFO: not resolving, not initializing cache", file=sys.stderr)
        cachecon = None
    elif not os.path.exists(args.listfile):
        print(
            f"WARNING: {args.listfile} does not exist, not resolving fileids")
        cachecon = None
    else:
        if os.path.exists(cachefile) and (os.path.getmtime(args.listfile) <= os.path.getmtime(cachefile)):
            print("INFO: fileid cache up to date, not updating", file=sys.stderr)
            cachecon = cache_open(cachefile)
        else:
            cachecon = cache_open(cachefile)
            cache_fileids(args.listfile, cachecon)

    # FIXME: handle more than one file
    file = args.files[0]

    name, ext = os.path.splitext(file)
    if ext == ".m2":
        from output.m2 import M2, KaitaiStruct
        target = M2.from_file(file)
    elif ext == ".skin":
        from output.skin import Skin, KaitaiStruct
        target = Skin.from_file(file)
    elif ext == ".skel":
        from output.skel import Skel, KaitaiStruct
        target = Skel.from_file(file)
    elif ext == ".blp":
        from output.blp import Blp, KaitaiStruct
        target = Blp.from_file(file)
    elif ext == ".bls":
        from output.bls import Bls, KaitaiStruct
        target = Bls.from_file(file)
    elif ext == ".wmo":
        from output.wmo import Wmo, KaitaiStruct
        target = Wmo.from_file(file)
    elif ext == ".wdt":
        from output.wdt import Wdt, KaitaiStruct
        target = Wdt.from_file(file)
    else:
        print(f"ERROR: don't know how to parse tile type {ext}")
        sys.exit(1)

    if args.output_type == "path":
        parsed = to_tree(target)
        print(f"# path = {file}")
        h = get_contenthash(file)
        print(f"# contenthash = {h}")

        pathdump(parsed, "", cachecon)
    elif args.output_type == "raw":
        print(ppretty(target, depth=99, seq_length=100,))
    elif args.output_type == "final":
        parsed = to_tree(target)
        print(ppretty(parsed, depth=99, seq_length=100,))
    elif args.output_type == "json":
        parsed = to_tree(target)
        json.dump(parsed, fp=sys.stdout, indent=2, sort_keys=True)
        print()  # newline at end
