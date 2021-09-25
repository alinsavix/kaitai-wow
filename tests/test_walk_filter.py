import logging
import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util

DATADIR = os.path.join(".", "test_data")

input_model = "levelup.m2"

# FIXME: can we find a smaller test file for this?

# behavior depends on whether keep or discard filters are provided,
# or both. Discard filters start with '!'
#
# no filter -- allow all
# only keep -- discard all but matching
# only discard --  keep all but matching
# both -- allow 'keep' matches, then discard all matching, then allow remaining


# make sure we're hiding things that should be hidden
def test_filter_keep(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--filter", "/model/version",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # make sure what we requested is there
    assert "/model/version =" in captured.out

    # make sure other things aren't
    assert "/model/textures" not in captured.out

    # make sure our elison messages aren't (sloppilly)  (FIXME: do better?)
    assert "elided" not in captured.out

    # check total lines
    assert len(captured.out.rstrip("\n").split("\n")) == 1


def test_filter_keep_multi(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--filter", "/model/version",
        "--filter", "/model/collision_sphere_radius",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # basically identical to the previous test
    # make sure what we want is there
    assert "/model/version =" in captured.out
    assert "/model/collision_sphere_radius" in captured.out

    # make sure other things aren't
    assert "/model/textures" not in captured.out

    # make sure our elison messages aren't (sloppilly)  (FIXME: do better?)
    assert "elided" not in captured.out

    # check total lines
    assert len(captured.out.rstrip("\n").split("\n")) == 2


def test_filter_discard(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--filter", "!/model/vertices",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # make sure what we don't want isn't there
    # this will also fail if the geometry elision text for this is there
    assert "/model/vertices" not in captured.out

    # and what we don't don't want is there
    assert "/model/textures" in captured.out

    # our elided text should still be there
    assert "elided" in captured.out


def test_filter_discard_multi(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--filter", "!/model/vertices",
        "--filter", "!/model/version",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # basically a dupe of the non-multi version
    # make sure what we don't want isn't there
    # this will also fail if the geometry elision text for this is there
    assert "/model/vertices" not in captured.out
    assert "/model/version =" not in captured.out

    # and what we don't don't want is there
    assert "/model/textures" in captured.out

    # our elided text should still be there
    assert "elided" in captured.out


def test_filter_keep_discard(capsys, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--filter", "/model/texture_weights/0",
        "--filter", "!/model/texture_weights",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # Make sure we got the part we wanted to keep
    assert "/model/texture_weights/0" in captured.out

    # and that we don't have the part we want filtered
    assert "/model/texture_weights/1" not in captured.out

    # and that other stuff still exists
    assert "/model/textures" in captured.out
