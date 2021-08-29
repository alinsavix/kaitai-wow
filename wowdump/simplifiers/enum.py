# simplifiers for enum values
import logging

def simplify_enum(d, _parent, _cachecon, _args):
    logger = logging.getLogger("simplify")
    logger.debug("using enum simplifier")

    return f"{d['value']}  # {d['name']}"


interpolation_type_re = r"interpolation_type$"
version_re = r"^/model/version$"


simplifiers = [
    (interpolation_type_re, simplify_enum),
    (version_re, simplify_enum),
]
