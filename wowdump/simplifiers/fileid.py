# simplifiers for file ids of various types
import csv
import sys
from typing import Optional, Union
import logging

# We can run without, we'll just be slow
try:
    import sqlite3
except ImportError:
    pass

def simplify_fileid(id: int, _parent, cachecon, args) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using fileid simplifier")
    logger.debug(f"type: {type(id)}   id: {id}")

    if not args.resolve or id <= 0:
        return f"{id}"

    c = cache_getfileid(id, cachecon)

    # if None, cache is not usable, so try the old fashioned way
    if c is None:
        c = csv_getfileid(id)

    if c is False:
        return f"{id}  # unresolved"
    else:
        return f"{id}  # {c}"


# FIXME: Should this be somewhere else?
def cache_getfileid(id: int, cachecon) -> Optional[Union[str, bool]]:
    if not cachecon:
        return None

    cur = cachecon.cursor()
    q = "SELECT name FROM file_ids WHERE id=?"

    try:
        res = cur.execute(q, [id]).fetchone()
    except sqlite3.Error as e:
        print(f"ERROR: Unexpected sqlite error: {e}", file=sys.stderr)
        return False

    # not in cache? Return false so that we know not to try to fall back to
    # the listfile, since the cache should be authoritative
    if res is None:
        return False

    return res[0]


# FIXME: Where should we -actually- look for this file?
def csv_getfileid(id: int):
    # FIXME
    return False
    try:
        with open("listfile.csv", 'r', newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                if int(row[0]) == id:
                    return f"{id}  # {row[1]}"
    except OSError:
        pass

    return False


fileids_re = r"^/chunks/\d+/chunk_data/([^/]+_)?file_data_ids/\d+$"
fileid_re = r"/([^/]+_)?file_data_id$"
mapfileid_re = r"^/chunks/\d+/chunk_data/map_fileids/\d+/[^/]+_file_data_id$"

simplifiers = [
    (fileid_re, simplify_fileid),
    (fileids_re, simplify_fileid),
    (mapfileid_re, simplify_fileid),
]
