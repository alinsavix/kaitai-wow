# simplifiers for color values
import argparse
import logging
from typing import Any, Dict

from . import SimplifierFunc


def simplify_irgb(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgb simplifier")

    r = int(d.r)
    g = int(d.g)
    b = int(d.b)

    return f"rgb({r}, {g}, {b})  # {r:02x}{g:02x}{b:02x}"

def simplify_irgb_short(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgb short simplifier")

    r = int(d.r)
    g = int(d.g)
    b = int(d.b)

    return f"#{r:02x}{g:02x}{b:02x}"

def simplify_irgba(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgba simplifier")
    r = int(d.r)
    g = int(d.g)
    b = int(d.b)
    a = int(d.a)

    return f"rgba({r}, {g}, {b}, {a})  # {r:02x}{g:02x}{b:02x}{a:02x}"

def simplify_irgba_short(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using irgba short simplifier")
    r = int(d.r)
    g = int(d.g)
    b = int(d.b)
    a = int(d.a)

    return f"#{r:02x}{g:02x}{b:02x}{a:02x}"


named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_irgb": simplify_irgb,
    "simplify_irgb_short": simplify_irgb_short,
    "simplify_irgba": simplify_irgba,
    "simplify_irgba_short": simplify_irgba_short,
}
