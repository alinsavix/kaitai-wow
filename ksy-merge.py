#!/usr/bin/env python3
import argparse
import os
import sys
import yaml

verbose = 0

def log(text):
    if verbose:
        print(text, file=sys.stderr)


# deep merge some dicts (in essence merging some yaml)
def merge_dict(y1, y2):
    if isinstance(y1, dict) and isinstance(y2, dict):
        for k, v in y2.items():
            if k not in y1:
                y1[k] = v
            else:
                y1[k] = merge_dict(y1[k], v)
    return y1


# wish I could just do this in the main loop, but apparently os.walk
# just utterly ignores file arguments, so we have to split it off
paths_handled = set()
def merge_file(yaml_data, file):
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


# iterate down through the filesystem and find files to merge
def recurse_merge(yaml_data, path):
    if os.path.isfile(path):
        return merge_file(yaml_data, path)

    # else
    for dirpath, _, files in os.walk(path):
        for name in files:
            fp = os.path.join(dirpath, name)
            merge_file(yaml_data, fp)


# VERY simple yaml merge. Everything is a deep merge. Conflicts resolve
# nondeterministically.
def parse_arguments():
    parser = argparse.ArgumentParser(
        prog = 'yaml-merge.py',
        description = 'Merge some yaml files',
    )

    # Not implemented yet
    parser.add_argument("-v", "--verbose", action="count", default=0)

    parser.add_argument(
        "files",
        help="specify files or directories to process",
        metavar="files",
        type=str,  # FIXME: Is there a 'file' type arg?
        nargs="+",
    )

    parsed_args = parser.parse_args()
    return parsed_args


def main():
    args = parse_arguments()

    # need a better way
    global verbose
    verbose = args.verbose

    # start with nothing, then add everything
    data = {}
    for f in args.files:
        recurse_merge(data, f)

    # The kaitai IDE can't cope with yaml multiline strings, so width=9999
    # will stop it from wrapping those lines when processing long heredocs
    print(yaml.dump(data, width=9999))


if __name__ == "__main__":
    sys.exit(main())
