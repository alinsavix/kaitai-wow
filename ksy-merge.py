#!/usr/bin/env python3
import argparse
import os
import re
import sys
import yaml
from ppretty import ppretty

from typing import Any, Dict, List, Set

verbose = 0

def log(text: str):
    if verbose:
        print(text, file=sys.stderr)


# We'll find things like:   id: name, type m2array<type>
# That needs to turn into, at the same level:
#
#   id: num_name
#   type: uint32
#   id: ofs_name
#   type: uint32
# instances:
#   name:
#     pos: ofs_name
#     type: type
#     repeat: expr
#     repeat-expr: num_name
# def massage_m2array(d):
#     pass

# dict_descent: accepts a dict (d), iterates the key:value sets, and if it
# finds a type: m2array<something>, then create a replacement block. If this
# returns a list, that list should be substituted in place of the thing that
# was being iterated, since we need to add things one level 'up'.
type_re = re.compile(r"^m2array<(.*)>$")
def dict_descent(d: Dict[str, Any], array_parent: bool, top: Dict[str, Any]):
    # if this dict has a 'type' key, we can (potentially) replace it.
    # Otherwise, we need to recurse
    log(f"check: {d}")
    if array_parent and "type" in d and "id" in d and isinstance(d["type"], str):
        log(f"thing: {array_parent}, {d['type']}, {d['id']}")
        m = type_re.search(d['type'])
        if m:
            arraytype = m.group(1)
            log(f"flagging for typereplace for type {arraytype}")
            # We don't really want to be inserting things into the middle
            # of the list while iterating, so generate a semaphore string
            # to hand back for eventual replacement.
            mm = type_re.search(arraytype)
            if not mm:
                replacetype = arraytype
            else:
                nested_type = mm.group(1)
                replacetype = f"{nested_type}_nested"

            return {
                "replarray": {
                    "type": replacetype,
                    "name": d['id'],   # might not need this, really
                    "orig": d.copy(),
                }
            }

        # FIXME: Are there conditions where we should keep searching here?
        return None

    # for k, v in d.items():
    for k in list(d.keys()):
        v = d[k]
        # If it's not something we can descend into, skip it
        if isinstance(v, dict):
            log(f"dict descent to {k}")
            dict_descent(v, False, top)
        elif isinstance(v, list):
            log(f"list descent to {k}")
            list_descent(v, d, top)

    return


nested_re = re.compile(r"(.*)_nested$")
def list_descent(d: List[Any], parent: Any, top: Dict[str, Any]):
    replacements = 0
    for i, v in enumerate(d):
        if isinstance(v, dict):
            log(f"dict descent to index {i}")
            r = dict_descent(v, True, top)
            log(f"r is {r}")
            if r is not None:
                log(f"r return, doing replacement string")
                d[i] = r
                replacements = 1
        elif isinstance(v, list):
            log(f"list descent to index {i}")
            list_descent(v, d, top)

    # If there were replacements, we want to rebuild the list in-place
    # with the replacements taken care of. There's probably a far cleaner
    # way to do this.
    log(f"entering d: {d}")
    if replacements:
        old = d.copy()
        del d[:]

        for i, v in enumerate(old):
            # For a normal m2array (e.g. m2array<u2> verts), this will
            # return, e.g..
            # {
            #     "replarray": {
            #         "type": "u2",
            #         "name": "verts", # might not need this, really
            #         "orig": {original defintiion},
            #     }
            # }
            #
            # For a nested m2array, this should return.. hmmm...
            # ... "u2_nested" as the type?"
            if isinstance(v, dict) and "replarray" in v:
                r = v["replarray"]
                # need to keep a conditional if there is one. Not sure the
                # best way to manage having/not having it depending on if
                # it exists, so instead we'll just have something always
                # true if there's not already a conditional. This could
                # probably be improved on!
                if "if" in r["orig"]:
                    conditional = r["orig"]["if"]
                else:
                    conditional = True

                name = r["name"]
                type = r["type"]
                m2arr_meta = [
                    {
                        "id": f"num_{name}",
                        "type": "u4",
                        "if": conditional,
                    },
                    {
                        "id": f"ofs_{name}",
                        "type": "u4",
                        "if": conditional,
                    }
                ]

                m2arr_instance = {
                    "id": name,
                    "type": type,
                    "pos": f"ofs_{name}",
                }

                if type == "str":
                    m2arr_instance.update({
                        "size": f"num_{name}",
                    })
                else:
                    m2arr_instance.update({
                        "repeat": "expr",
                        "repeat-expr": f"num_{name}",
                    })

                m2arr_instance.update({"if": conditional, })

                # First, do the in-place replacement by providing our
                # own version
                d.extend(m2arr_meta)

                # And now look at parent.instances (create it if it doesn't
                # exist) and insert our actual instance there. (this is
                # annoying)
                if not isinstance(parent, dict):
                    log("WARNING: Trying to make instance, but wrong parent")
                    continue

                if "instances" not in parent:
                    parent["instances"] = {}

                parent["instances"][name] = m2arr_instance

                # and finally, if it's a nested m2array type, create a
                # top-level type for the inner part, because kaitai
                # can't currently do nested/multi-dimensional arrays
                m = nested_re.search(type)
                if not m:
                    continue

                # We have a nested m2array, handle it
                arraytype = m.group(1)
                if "types" not in top:
                    top["types"] = {}

                # Do we already have this type?
                if type in top["types"]:
                    log(f"inner type {type} already exists, not recreating")
                    continue

                top["types"][type] = {}
                t = top["types"][type]
                t["seq"] = [
                    {
                        "id": f"num_{name}",
                        "type": "u4",
                        "if": conditional,
                    },
                    {
                        "id": f"ofs_{name}",
                        "type": "u4",
                        "if": conditional,
                    }
                ]

                m2arr_inner_instance = {
                    "id": type,
                    "type": arraytype,
                    "pos": f"ofs_{name}",
                    "repeat": "expr",
                    "repeat-expr": f"num_{name}",
                    "if": conditional,
                }

                if "instances" not in t:
                    t["instances"] = {}
                t["instances"]["inner"] = m2arr_inner_instance
            else:
                log(f"appending v: {v}")
                d.append(v)

    log(f"returning d: {d}")
    return


# deep merge some dicts (in essence merging some yaml)
# FIXME: Sanity check what we're doing with arrays
def merge_dict(y1: Any, y2: Any):
    if not isinstance(y1, dict) or not isinstance(y2, dict):
        return y1

    for k, v in y2.items():
        if k not in y1:
            y1[k] = v
        else:
            y1[k] = merge_dict(y1[k], v)

    return y1


# wish I could just do this in the main loop, but apparently os.walk
# just utterly ignores file arguments, so we have to split it off
paths_handled: Set[str] = set()
def merge_file(yaml_data: Dict[str, str], file: str):
    if file in paths_handled:
        log(f"already did '{file}'', skipping")
        return

    if not file.lower().endswith(".ksy"):
        log(f"not ksy, skipping: {file}")
        return

    log(f"merging '{file}'")
    paths_handled.add(file)

    with open(file, "r") as f:
        data = yaml.safe_load(f)
        if data and "meta" in data and "include" in data["meta"]:
            for incl in data["meta"]["include"]:
                log(f"processing include '{incl}' from '{file}'")
                recurse_merge(yaml_data, incl)

            del data["meta"]["include"]

        merge_dict(yaml_data, data)


# iterate down through the filesystem and find files to merge. This
# originally descended through nested subdirectories, but now we just
# have it doing the specific directory named, to get a bit more
# granularity with our includes.
#
# FIXME: Eventually we want to filter this by types that are actually used!
def recurse_merge(yaml_data: Dict[Any, Any], path: str):
    if os.path.isfile(path):
        return merge_file(yaml_data, path)

    # else
    with os.scandir(path) as filepaths:
        for fp in filepaths:
            if not fp.is_file():
                continue
            merge_file(yaml_data, os.path.join(path, fp.name))


# VERY simple yaml merge. Everything is a deep merge. Conflicts resolve
# nondeterministically.
def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='ksy-merge.py',
        description='Merge some yaml files',
    )

    # Not implemented yet
    parser.add_argument("-v", "--verbose", action="count", default=0)

    parser.add_argument(
        "--deps-file",
        type=str,
        default=None,

        help="file to output dependency information to",
    )

    parser.add_argument(
        "--deps-target",
        type=str,
        default=None,

        help="target name to use for created dependency,"
    )

    parser.add_argument(
        "--deps-only",
        action="store_true",
        default=False,

        help="only generate dependencies, don't output merged file",
    )


    parser.add_argument(
        "files",
        help="specify files or directories to process",
        metavar="files",
        type=str,  # FIXME: Is there a 'file' type arg?
        nargs="+",
    )

    parsed_args = parser.parse_args()

    if parsed_args.deps_target is None:
        parsed_args.deps_target = parsed_args.files[0]

    return parsed_args


def main():
    args = parse_arguments()

    # need a better way
    global verbose
    verbose = args.verbose

    # start with nothing, then add everything
    data: Dict[Any, Any] = {}
    for f in args.files:
        recurse_merge(data, f)

    dict_descent(data, False, data)

    # The kaitai IDE can't cope with yaml multiline strings, so width=9999
    # will stop it from wrapping those lines when processing long heredocs
    if not args.deps_only:
        print(yaml.dump(data, width=9999))
        # log(ppretty(data, depth=99, seq_length=50))

    if args.deps_file is not None:
        with open(args.deps_file, "w") as f:
            # FIXME: using a global sucks. don't use a global
            handled = " \\\n    ".join(paths_handled)
            print(f"{args.deps_target}: \\", file=f)
            print("    " + handled, file=f)

if __name__ == "__main__":
    sys.exit(main())
