#!/usr/local/bin/python3
import os
import sys
from ppretty import ppretty
import inspect
from m2 import *

# This script is what's known as "awful". It's brute force. It does
# everything wrong. It probably doesn't even taste like chocolate.
# But should at least give a baseline for dumping interesting info
# out of interesting files, even if it *is* garbage at the moment.
#
# Also, did I mention it's garbage?

DEFAULT_TARGET = "testfiles/spectraltiger.m2"

# FIXME: Turn these into proper verbosity flags
do_verbose = 0
do_debug = 0
showtree = 0
do_disposition = 0
do_finaldump = 1


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


if __name__ == "__main__":
    try:
        targetfile = sys.argv[1]
        print(f"Using specified target file {targetfile}", flush=True)
    except IndexError:
        targetfile = DEFAULT_TARGET
        print(f"WARNING: Using default target file {targetfile}", flush=True)

    target = M2.from_file(targetfile)

    parsed = to_tree(target)
    if do_finaldump:
        print(ppretty(parsed, depth=99, seq_length=100,))


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
