# simplifier to display coordinates as (x,y) or similar
import argparse
import logging
from typing import Any, Dict

from . import SimplifierFunc


def simplify_xyz(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xyz simplifier")

    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    z = round(d.z, args.precision)
    return f"xyz({x}, {y}, {z})"


def simplify_wxyz(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using wxyz simplifier")

    w = round(d.w, args.precision)
    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    z = round(d.z, args.precision)
    return f"wxyz({w}, {x}, {y}, {z})"


def simplify_xy(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xy simplifier")

    x = round(d.x, args.precision)
    y = round(d.y, args.precision)
    return f"xy({x}, {y})"


def simplify_nested_xy(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using nested xy simplifier")

    x = d.x.value
    y = d.y.value
    return f"xy({x}, {y})"


named_simplifiers: Dict[str, SimplifierFunc] = {
    "simplify_xy": simplify_xy,
    "simplify_xyz": simplify_xyz,
    "simplify_wxyz": simplify_wxyz,
    "simplify_nested_xy": simplify_nested_xy,
}
