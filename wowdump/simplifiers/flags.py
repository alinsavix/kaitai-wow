# simplify flags
import logging
from ..dumputil import kttree

# FIXME: Should the output be inside { } or something?
def simplify_flags(d, _parent, _cachecon, _args):
    logger = logging.getLogger("simplify")
    logger.debug("using flags simplifier")

    # Somethihg named flags but isn't actually flags
    if isinstance(d, int):
        return str(d)

    d = kttree(d)

    if not isinstance(d, dict):
        return d

    flags = []
    for k, v in d.items():
        if v:
            flags.append(k)

    if len(flags) == 0:
        return "none"

    return ", ".join(flags)


flags_re = r"/(global_)?flags$"


simplifiers = [
    (flags_re, simplify_flags),
]