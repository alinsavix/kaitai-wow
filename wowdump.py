#!/usr/local/bin/python3
import argparse
import csv
import json
import os
import re
import sys
from ppretty import ppretty
import inspect

# This script is what's known as "awful". It's brute force. It does
# everything wrong. It probably doesn't even taste like chocolate.
# But should at least give a baseline for dumping interesting info
# out of interesting files, even if it *is* garbage at the moment.
#
# Also, did I mention it's garbage?

# DEFAULT_TARGET = "testfiles/spectraltiger.m2"
DEFAULT_TARGET = "testfiles/staff_2h_draenorcrafted_d_02_c.m2"

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


def to_tree(obj, path=""):
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
    ^/(global_)?flags$
''', re.VERBOSE)

bbox_re = re.compile(r'''
    ^/model/(bounding_box|collision_box)/(min|max)$
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

seq_bbox_re = re.compile(r'''
    ^/model/sequences/\d+/bounds/extent/(min|max)$
''', re.VERBOSE)

verts_vec_re = re.compile(r'''
    ^/model/vertices/\d+/(normal|pos)$
''', re.VERBOSE)

verts_texcoords_re = re.compile(r'''
    /model/vertices/\d+/tex_coords/\d+$
''', re.VERBOSE)

# FIXME: Can we make these behave better straight out of kaitai?
nested_xy_re = re.compile(r'''
    /model/particle_emitters/\d+/multi_texture_param\d/\d+$
''', re.VERBOSE)

fileid_re = re.compile(r'''
    ^/chunks/\d+/chunk_data/([^/]+_)?file_data_ids/\d+$
''', re.VERBOSE)

def simplify_xyz(d):
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    z = round(d["z"], args.precision)
    return f"xyz({x}, {y}, {z})"

def simplify_wxyz(d):
    w = round(d["w"], args.precision)
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    z = round(d["z"], args.precision)
    return f"wxyz({w}, {x}, {y}, {z})"

def simplify_xy(d):
    x = round(d["x"], args.precision)
    y = round(d["y"], args.precision)
    return f"xy({x}, {y})"

def simplify_nested_xy(d):
    x = d["x"]["value"]
    y = d["y"]["value"]
    return f"xy({x}, {y})"

def simplify_irgb(d):
    r = int(d["r"])
    g = int(d["g"])
    b = int(d["b"])

    return f"rgb({r}, {g}, {b})  # {r:02x}{g:02x}{b:02x}"

# FIXME: Should the output be inside { } or something?
def simplify_flags(d):
    if not isinstance(d, dict):
        return d

    flags = []
    for k, v in d.items():
        if v:
            flags.append(k)

    if len(flags) == 0:
        return "none"

    return ", ".join(flags)


# FIXME: This gonna be slow until database or caching
def resolve_fileid(id):
    if id <= 0:
        return f"{id}"

    with open('listfile.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if int(row[0]) == id:
                return f"{id}  # {row[1]}"

    return f"{id}  # unresolved"


simplifications = [
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
    (verts_texcoords_re, simplify_xy),
    (fileid_re, resolve_fileid)
]

def check_simplify(path):
    if not args.simplify:
        return None

    for r in simplifications:
        if r[0].search(path):
            return r[1]

    return None


def pathdump(d, path=""):
    # This is kind of a lame way to get a loop that handles both lists
    # and dicts, but is there a better way?
    if isinstance(d, dict):
        things = sorted(d.keys())
    elif isinstance(d, list):
        things = range(0, len(d))

    for k in things:
        workpath = f"{path}/{k}"
        thing = d[k]

        # if we have ofs_xxx or num_xxx, and *also* just have xxx,
        # we don't need the offset/size anymore
        if args.hide_unneeded and isinstance(k, str) and (k.startswith("ofs_") or k.startswith("num_")):
            s = k[len("ofs_"):]
            if s in things:
                continue

        s = check_simplify(workpath)
        if s:
            simplified = s(thing)
            print(f"{workpath} = {simplified}")
        elif isinstance(thing, dict) or isinstance(thing, list):
            pathdump(thing, workpath)
        else:
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
        prog="decimator",
        description="A pipeline in a box for decimating lots of objects",
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
        # help="Read objects and prepare them for decimation",
    )

    parser.add_argument(
        "--disposition",
        action='store_const',
        const=True,
        default=False,
        # help="Read objects and prepare them for decimation",
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
        "--precision",
        action='store',
        type=int,
        default=6,
        help="decimal digits to include on simplified floats"
    )

    parser.add_argument(
        "--output_type",
        "-t",
        choices=["path", "json", "final", "raw", ],
        default="path",
        help="select output type (default: %(default)s)",
    )

    parser.add_argument(
        "file",
        nargs='?',
        help="input file to be processed",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_arguments()

    if args.file is None:
        args.file = DEFAULT_TARGET
        print(
            f"WARNING: Using default target file {args.file}", flush=True, file=sys.stderr)

    name, ext = os.path.splitext(args.file)
    if ext == ".m2":
        from output.m2 import M2, KaitaiStruct
        target = M2.from_file(args.file)
    elif ext == ".skin":
        from output.skin import Skin, KaitaiStruct
        target = Skin.from_file(args.file)
    elif ext == ".skel":
        from output.skel import Skel, KaitaiStruct
        target = Skel.from_file(args.file)
    elif ext == ".blp":
        from output.blp import Blp, KaitaiStruct
        target = Blp.from_file(args.file)
    elif ext == ".bls":
        from output.bls import Bls, KaitaiStruct
        target = Bls.from_file(args.file)

    parsed = to_tree(target)

    if args.output_type == "path":
        pathdump(parsed)
    elif args.output_type == "raw":
        print(ppretty(target, depth=99, seq_length=100,))
    elif args.output_type == "final":
        print(ppretty(parsed, depth=99, seq_length=100,))
    elif args.output_type == "json":
        json.dump(parsed, fp=sys.stdout, indent=2, sort_keys=True)
        print()  # newline at end

# print("thing")
# x = target.chunks[0].data
# print("thing2")

# x = target.chunks[0].data
# print(type(x))

# # x = target.chunks[0].data.data
# # print(dir(x))
# # print(x)
# sys.exit(0)


# print(f"root type {type(x)}")
# for d in dir(x):
#     if d.startswith("_"):
#         continue

#     v = getattr(x, d)
#     if inspect.isbuiltin(v):
#         continue

#     if isinstance(v, type):
#         continue

#     print(f"{d} type {type(v).__name__}")
#     print(f"builtin: {inspect.isbuiltin(v)}")
#     print(f"method: {inspect.ismethod(v)}")

# from ppretty import ppretty
# print(ppretty(target, depth=99, seq_length=50))
# print(ppretty(to_tree(target)))
