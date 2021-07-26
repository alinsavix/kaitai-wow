# Load up a bunch of simplifiers and the regexes that trigger them
#
# FIXME: get info about what to simplify from ksy metadata instead
import re
from importlib import import_module
import wowdump.simplifiers

simplifiers = set()

simplifier_list = frozenset([
    "remove",
    "color",
    "coordinates",
    "shaderid_m2",
    "shaderid_wmo",
])

for s in simplifier_list:
    ss = import_module("." + s, package="wowdump.simplifiers")
    for sss in ss.simplifiers:
        compiled_re = re.compile(sss[0], re.VERBOSE)
        simplifiers.add((compiled_re, sss[1]))

print(simplifiers)
