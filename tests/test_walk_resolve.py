import logging
import os

from typing import List

import pytest
from pytest_html import extras

from testutil import util

DATADIR = os.path.join(".", "test_data")
input_model = "levelup.m2"

# FIXME: We also probably want unit tests for resolution & caching

# levelup.m2 has these references in it:
#   167220;spells/yellow_glow_dim2.blp
#   197639;world/generic/gnome/activedoodads/gnomemachine/yellow_star_dim.blp
#   494151;spells/levelup/levelup00.skin
#
# and this one should be there, but we removed it to test missing fdids:
#   166153;spells/firering4.blp


# make sure we can resolve fdids
def test_resolve(capsys, extra):
    import wowdump
    wowdump.main([
        "--resolve",
        "--listfile", os.path.join(DATADIR, "listfile_minimal.csv"),
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # Make sure we actually got fdid resolution
    assert "skin_file_data_ids/0 = 494151  # spells/levelup/levelup00.skin" in captured.out
    assert "file_data_ids/0 = 167220  # spells/yellow_glow_dim2.blp" in captured.out

    # Make sure we correctly get 'unresolved' on things that shouldn't exist
    assert "file_data_ids/2 = 166153  # unresolved" in captured.out


# make sure we don't resolve fdids when we don't want to
def test_resolve_noresolve(capsys, caplog, extra):
    import wowdump
    wowdump.main([
        "--no-resolve",
        "--listfile", "/this/does/not/exist",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # verify we don't get an error on opening listfile (because we shouldn't
    # be trying to open it at all)
    assert "does not exist, not resolving fileids" not in caplog.text

    # nothing should show 'unresolved' if resolution isn't enabled
    assert "  # unresolved" not in captured.out

    # make sure we didn't somehow resolve anything, too
    assert "  # spells/yellow_glow_dim2.blp" not in captured.out


# make sure we throw a warning if the listfile doesn't exist, but make sure
# we continue regardless
def test_resolve_missing_listfile(capsys, caplog, extra):
    import wowdump
    wowdump.main([
        "--resolve",
        "--listfile", "/this/does/not/exist",
        os.path.join(DATADIR, input_model),
    ])
    captured = capsys.readouterr()

    # verify we get our warning for the missing listfile
    assert ("root", logging.WARNING,
            "/this/does/not/exist does not exist, not resolving fileids") in caplog.record_tuples

    # make sure we're correctly; showing things as "unresolved"
    # FIXME: Do we want 'unresolved', or nothing?
    assert "skin_file_data_ids/0 = 494151  # unresolved" in captured.out