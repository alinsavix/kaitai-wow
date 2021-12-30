# simplifiers for file ids of various types
import argparse
import logging
from typing import Any, Dict, List

from .. import csvcache
from . import SimplifierFunc


def simplify_fileid(id: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fileid simplifier")
    logger.debug(f"type: {type(id)}   id: {id}")

    if not args.resolve or id <= 0:
        return f"{id}"

    c = csvcache.get("listfile").get_by_id(id)

    if c is None:
        return f"{id}  # unresolved"
    else:
        return f"{id}  # {c}"

def simplify_fileid_short(id: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fileid short simplifier")
    logger.debug(f"type: {type(id)}   id: {id}")

    if not args.resolve or id <= 0:
        return f"{id}"

    c = csvcache.get("listfile").get_by_id(id)

    if c is None:
        return f"{id}  # unresolved"
    else:
        last = c.split("/")[-1]
        return f"{id}  # {last}"


named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_fileid": simplify_fileid,
}
