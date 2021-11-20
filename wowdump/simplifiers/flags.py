# simplify flags
import argparse
import logging
from typing import Any, List

from ..dumputil import kttree
from . import SimplifierUncompiled


# FIXME: Should the output be inside { } or something?
def simplify_flags(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using flags simplifier")

    # Somethihg named flags but isn't actually flags
    if isinstance(d, int):
        return str(d)

    d = kttree(d)

    if not isinstance(d, dict):
        return str(d)

    flags = []
    for k, v in d.items():
        if v:
            flags.append(k)

    if len(flags) == 0:
        return "none"

    return ", ".join(flags)


flags_re = r"/(global_)?flags(2)?$"


simplifiers: List[SimplifierUncompiled] = [
    (flags_re, simplify_flags),
]
