# simplifiers for file ids of various types
from .. import csvcache

import logging


def simplify_fileid(id: int, _parent, args) -> str:
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

def simplify_fileid_short(id: int, _parent, args) -> str:
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


fileids_re = r"^/chunks/\d+/chunk_data/([^/]+_)?(file_data_ids|fdids)/\d+$"
fileid_re = r"/([^/]+_)?(file_data_id|fdid)$"
mapfileid_re = r"^/chunks/\d+/chunk_data/map_fileids/\d+/[^/]+_(file_data_id|fdid)$"

simplifiers = [
    (fileid_re, simplify_fileid),
    (fileids_re, simplify_fileid),
    (mapfileid_re, simplify_fileid),
]
