# kaitaistruct makes it hard to type the actual report generator (we should
# really fix that), so here's a simple type stub so other things don't
# complain when we completely ignore it.
import argparse

from .dumputil import DataOutput

def wmo(args: argparse.Namespace, file: str, out: DataOutput) -> None:
    pass
