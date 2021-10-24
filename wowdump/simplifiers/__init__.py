# Load up a bunch of simplifiers and the regexes that trigger them
#
# FIXME: get info about what to simplify from ksy metadata instead
import re
from importlib import import_module
# import wowdump.simplifiers

simplifiers = set()

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

for s in simplifier_list:
    # We need to specify ourselves as package= for relative imports to work
    ss = import_module("." + s, package="wowdump.simplifiers")
    for sss in ss.simplifiers:  # type: ignore
        compiled_re = re.compile(sss[0], re.VERBOSE)
        simplifiers.add((compiled_re, sss[1]))


# Check to see if a given path has a simplifier, return the appropriate
# simplifier function if there's a match.
def check_simplify(path: str):
    for r in simplifiers:
        if r[0].search(path):
            return r[1]

    return None


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
