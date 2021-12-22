# Load up a bunch of simplifiers and the regexes that trigger them

import argparse
import re
from importlib import import_module
from typing import (Any, Callable, Dict, List, Optional, Pattern, Set, Tuple,
                    Type, cast)

from ..ksymeta import getmeta

SimplifierFunc = Callable[[Any, Any, argparse.Namespace], Optional[str]]

Simplifier = Tuple[Pattern[str], SimplifierFunc]

SimplifierUncompiled = Tuple[str, SimplifierFunc]

simplifiers: Set[Simplifier] = set()

simplifier_funcs: Dict[str, SimplifierFunc] = {}

simplifier_list = frozenset([
    "bones",
    "color",
    "coordinates",
    "enum",
    "events",
    "fileid",
    "flags",
    "remove",
    "shaderid_m2",
    "shaderid_wmo",
])


def init_simplify() -> None:
    global simplifiers
    simplifiers = set()

    global simplifier_funcs
    simplifier_funcs = {}

    for s in simplifier_list:
        # We need to specify ourselves as package= for relative imports to work
        ss = import_module("." + s, package="wowdump.simplifiers")
        sl: List[SimplifierUncompiled] = getattr(ss, "simplifiers", [])
        for sss in sl:
            compiled_re = re.compile(sss[0], re.VERBOSE)
            simplifiers.add((compiled_re, sss[1]))

        sd: Dict[str, SimplifierFunc] = getattr(ss, "named_simplifiers", {})
        for funcname, func in sd.items():  # type: ignore
            simplifier_funcs[funcname] = func


# Check to see if a given path has a simplifier, return the appropriate
# simplifier function if there's a match.
#
# FIXME: needs a bit of debugging
def check_simplify(
        path: str, filetype: str, dataname: str,
        datatype: Optional[type] = None,
        parenttype: Optional[type] = None
) -> Tuple[Optional[SimplifierFunc], bool]:
    if filetype and datatype:
        type = datatype.__name__.lower()
        parent = parenttype.__name__.lower() if parenttype else None

        meta = getmeta(filetype, type)
        if meta:
            if "simplifier" in meta:
                s = meta["simplifier"]
                if s in simplifier_funcs:
                    return simplifier_funcs[s], False

            if "simplifier_each" in meta:
                s = meta["simplifier_each"]
                if s in simplifier_funcs:
                    return simplifier_funcs[s], True

        if parent:
            meta = getmeta(filetype, f"{parent}.{dataname}")
            if meta:
                if "simplifier" in meta:
                    s = meta["simplifier"]
                    if s in simplifier_funcs:
                        return simplifier_funcs[s], False

                if "simplifier_each" in meta:
                    s = meta["simplifier_each"]
                    if s in simplifier_funcs:
                        return simplifier_funcs[s], True

    for r in simplifiers:
        if r[0].search(path):
            return r[1], False

    return None, False


if len(simplifiers) == 0 and len(simplifier_funcs) == 0:
    init_simplify()


# Notes from the original implementation:
#
# These next bits are an attempt to simplify certain structures into
# a more human-readable form. This is ugly and stupid and needs to
# be hand-maintained. We might be able to do better with some additional
# metadata out of kaitai or such, but for now, this is a quick and dirty
# "but I want to be able to read this" solution. There's probably better
# bad ways to do it, and definitely better not-bad ways to do it, but
# this works. For now. Until it offends my sight just a little too much
# and gets torn out by the roots (just like my hair)   --A
