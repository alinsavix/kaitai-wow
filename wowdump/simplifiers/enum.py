# simplifiers for enum values
import argparse
import logging
from typing import Any, Dict

from . import SimplifierFunc


def simplify_enum(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using enum simplifier")

    # If a field is an enum, but a value for the specific integer doesn't
    # exist, kaitai just returns an int, rather than an enum value without
    # an enum name.
    if isinstance(d, int):
        return f"{d}"

    return f"{d.value}  # {d.name}"


named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_enum": simplify_enum,
}
