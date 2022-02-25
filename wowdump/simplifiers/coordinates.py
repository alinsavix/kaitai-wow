# simplifier to display coordinates as (x,y) or similar
import argparse
import logging
from typing import Any, Dict

from . import SimplifierFunc


# sucks having to do this, but basically we want to be able to output
# a floating point number with `precision` digits, but we want numbers
# that have a shorter representation (i.e. less trailing zeroes) to be
# shorter, and under no circumstances do we want scientific notation.
# Is there a better way to do this? I truly have no idea.
def ffmt(f: float, precision: int) -> str:
    f2 = round(f, precision)
    f3 = f"{f2:.{precision}f}"
    f4 = f3.rstrip("0")
    if f4.endswith("."):
        f4 += "0"

    return f4

def simplify_xyz(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xyz simplifier")

    x = ffmt(d.x, args.precision)
    y = ffmt(d.y, args.precision)
    z = ffmt(d.z, args.precision)
    return f"xyz({x}, {y}, {z})"


def simplify_wxyz(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using wxyz simplifier")

    w = ffmt(d.w, args.precision)
    x = ffmt(d.x, args.precision)
    y = ffmt(d.y, args.precision)
    z = ffmt(d.z, args.precision)

    # return f"wxyz({w:.{p+1}g}, {x:.{p+1}g}, {y:.{p+1}g}, {z:.{p+1}g})"
    return f"wxyz({w}, {x}, {y}, {z})"

def simplify_xy(d: Any, _parent: Any, args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using xy simplifier")

    x = ffmt(d.x, args.precision)
    y = ffmt(d.y, args.precision)
    return f"xy({x}, {y})"


# FIXME: should this take into account precision?
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
