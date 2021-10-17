# simplifiers for bone-related things (when we have them)
import logging

def simplify_fourbone(d, _parent, _cachecon, _args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fourbone simplifier")
    return f"[ {d[0]}, {d[1]}, {d[2]}, {d[3]} ]"

def simplify_fourbone_m2arr(d, _parent, _cachecon, _args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fourbone m2arr simplifier")
    return f"[ {d.value[0]}, {d.value[1]}, {d.value[2]}, {d.value[3]} ]"


fourbone_re = r"^/model/vertices/\d+/(bone_indices|bone_weights)$"
fourbone_skin_re = r"^/skin/bones/\d+$"


simplifiers = [
    (fourbone_re, simplify_fourbone),
    (fourbone_skin_re, simplify_fourbone_m2arr)
]
