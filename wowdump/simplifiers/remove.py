# simplifier to just remove stuff
import argparse
import logging
from typing import Any, Dict, Optional

from . import SimplifierFunc


def simplify_remove(d: Any, _parent: Any, _args: argparse.Namespace) -> Optional[str]:
    logger = logging.getLogger("simplify")
    logger.debug("using remove simplifier")
    return None


named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_remove": simplify_remove,
}
