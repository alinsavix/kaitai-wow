import logging
import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util
import wowdump

DATADIR = os.path.join("tests", "test_data")

input_model = "levelup.m2"

# FIXME: can we find a smaller test file for this?

# make sure we're hiding things that should be hidden
def test_unneeded_hide(request, capsys, extra):
    ret = wowdump.main([
        "--no-resolve",
        "--no-simplify",
        "--hide-unneeded",  # the default
        os.path.join(request.config.rootdir, DATADIR, input_model),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()

    assert "/model/num_bone_lookup" not in captured.out


def test_unneeded_nohide(request, capsys, extra):
    ret = wowdump.main([
        "--no-resolve",
        "--no-simplify",
        "--no-hide-unneeded",  # the default
        os.path.join(request.config.rootdir, DATADIR, input_model),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()

    assert "/model/num_bone_lookup" in captured.out
