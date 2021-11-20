# simplifier to just remove stuff
import argparse
import logging
from typing import Any, List, Optional

from . import SimplifierUncompiled


def simplify_remove(d: Any, _parent: Any, _args: argparse.Namespace) -> Optional[str]:
    logger = logging.getLogger("simplify")
    logger.debug("using remove simplifier")
    return None


# Runtime data that doesn't exist in WoW data files (usually just zeroes that
# are filled in after the structure is loaded into memory verbatim
runtime_re = r"/runtime_data$"


# Values believed to be unused
unused_re = r"unused\d*$"

# Chunk type identifiers before being reversed for human consumption
raw_chunk_re = r"chunk_type_raw$"


# mapping
simplifiers: List[SimplifierUncompiled] = [
    (runtime_re, simplify_remove),
    (unused_re, simplify_remove),
    (raw_chunk_re, simplify_remove),
]
