import logging
import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util

DATADIR = os.path.join("tests", "test_data")
input_model = "levelup.m2"

# FIXME: There's a lot of simplifiers ... should we give them all a unit test?
# (yes, probably)

# FIXME: can we find a smaller test file for this?


# make sure simplifier output seems to be working
def test_simplify(request, capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--simplify",  # also the default
        os.path.join(request.config.rootdir, DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # make sure we got our simplifier output as expected
    assert "/model/bounding_box/max = xyz(8.763622, 2.173703, 9.998041)" in captured.out


# make sure we don't resolve fdids when we don't want to
def test_simplify_nosimplify(request, capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--no-simplify",
        os.path.join(request.config.rootdir, DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # FIXME: can/should we check for -any- simplifier in the output?
    assert " = xyz(" not in captured.out
