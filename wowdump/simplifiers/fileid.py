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


fileids_re = r"^/chunks/\d+/chunk_data/([^/]+_)?file_data_ids/\d+$"
fileid_re = r"/([^/]+_)?file_data_id$"
mapfileid_re = r"^/chunks/\d+/chunk_data/map_fileids/\d+/[^/]+_file_data_id$"

simplifiers = [
    (fileid_re, simplify_fileid),
    (fileids_re, simplify_fileid),
    (mapfileid_re, simplify_fileid),
]
