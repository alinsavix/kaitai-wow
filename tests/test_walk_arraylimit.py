import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util

DATADIR = os.path.join(".", "test_data")
input_model = "levelup.m2"

# Make sure that arraylimit works for changing the array limit
def test_geometry_arraylimit(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve", "--geometry", "--arraylimit", "50",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # Make sure we don't get the elision message
    assert "geometry data elided, use --geometry to include" not in captured.out

    # verify we get geometry data up to our limit
    assert "/model/vertices/49" in captured.out

    # verify we don't get more than our limit
    assert "/model/vertices/50" not in captured.out

    # verify we get the elision message
    assert "/model/vertices/... = [50 elided of 100 total]" in captured.out
