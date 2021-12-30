import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

# class KsyMetaType:
#     type: str
#     simplifier: Optional[str] = None

__meta: Dict[str, Dict[str, Any]] = {}

# meta (at the moment) is stored as yaml in the 'filetypes' directory.
# Not having meta (at the moment) is not an error .
def __loadmeta(filetype: str) -> Dict[str, Any]:
    logger = logging.getLogger("ksymeta")
    basepath = os.path.dirname(os.path.realpath(__file__))
    metapath = Path(basepath) / "filetypes" / f"{filetype}.yaml"

    meta: Dict[str, Any]
    if metapath.exists():
        with open(metapath, "r") as f:
            meta = yaml.safe_load(f)
    else:
        logger.warning(f"couldn't load metadata for filetype {filetype}")
        meta = {}

    return meta


def getmeta(filetype: str, datatype: str) -> Optional[Dict[str, Any]]:
    global __meta

    if filetype not in __meta:
        __meta[filetype] = __loadmeta(filetype)

    if datatype in __meta[filetype]:
        return __meta[filetype][datatype]

    return None
