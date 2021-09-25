import logging
import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util

DATADIR = os.path.join(".", "test_data")

input_model = "levelup.m2"
input_hash = "d1b1a625d1396a83b907319265346580"

# FIXME: can we find a smaller test file for this?


# make sure simplifier output seems to be working
def test_contenthash(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--no-simplify",  # don't do more work than needed
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # contenthash should always be the first line, and should always be there
    assert captured.out.split("\n")[0] == "/contenthash = d1b1a625d1396a83b907319265346580"
