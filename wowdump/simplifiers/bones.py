# simplifiers for bone-related things (when we have them)
import argparse
import logging
from typing import Any, Dict, List

from . import SimplifierFunc, SimplifierUncompiled


def simplify_fourbone(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fourbone simplifier")
    return f"[ {d[0]}, {d[1]}, {d[2]}, {d[3]} ]"

def simplify_fourbone_m2arr(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fourbone m2arr simplifier")
    return f"[ {d.value[0]}, {d.value[1]}, {d.value[2]}, {d.value[3]} ]"


fourbone_skin_re = r"^/skin/bones/\d+$"

# FIXME: need this for /skin/bones for now, until we figure out how to
# actually manage that better
simplifiers: List[SimplifierUncompiled] = [
    (fourbone_skin_re, simplify_fourbone_m2arr)
]

named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_fourbone": simplify_fourbone,
    "simplify_fourbone_m2arr": simplify_fourbone_m2arr,
}
