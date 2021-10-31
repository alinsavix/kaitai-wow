import logging
import os
from pathlib import Path

from wowdump import csvcache

DATADIR = os.path.join("tests", "test_data")

# levelup.m2 has these references in it (notes from test_walk_resolve.py):
#   167220;spells/yellow_glow_dim2.blp
#   197639;world/generic/gnome/activedoodads/gnomemachine/yellow_star_dim.blp
#   494151;spells/levelup/levelup00.skin
#
# and this one should be there, but we removed it to test missing fdids:
#   166153;spells/firering4.blp


# FIXME: need tests also for:
#   - correct behavior re-initing from None -> not none
#   - correct behavior re-initing from not none -> none
#   - correct behavior initing when the cache is up to date
#   - correct behavior initing when the cache is out of date
#   - correct behavior initing when the cache doesn't exist

# make sure we throw a warning if the listfile doesn't exist, but make sure
# we continue regardless
def test_csvcache_missing_listfile(request, capsys, caplog, extra):
    # c = csvcache.init("listfile_missing", os.path.join(
    #     request.config.rootdir, DATADIR, input_model))
    c = csvcache.init("listfile_missing", "/this/does/not/exist")

    assert isinstance(c, csvcache.ListfileCache)
    assert c.nocache is True

    d = c.get_by_id(197639)
    assert d is None

    # verify we get our warning for the missing listfile
    assert ("csvcache", logging.WARNING,
            str(Path("/this/does/not/exist")) + " does not exist, not resolving fileids") in caplog.record_tuples


# make sure we handle the 'no cache' form
def test_csvcache_nullcache(request, capsys, caplog, extra):
    c = csvcache.init("listfile_null", None)

    assert isinstance(c, csvcache.ListfileCache)
    assert c.nocache is True

    d = c.get_by_id(197639)
    assert d is None

    assert len(caplog.record_tuples) == 0



# make sure we can resolve fdids
def test_csvcache_resolve(request, capsys, extra):
    c = csvcache.init("listfile", os.path.join(
        request.config.rootdir, DATADIR, "listfile_minimal.csv"))

    assert isinstance(c, csvcache.ListfileCache)
    assert c.nocache is False

    d = c.get_by_id(197639)
    assert d == "world/generic/gnome/activedoodads/gnomemachine/yellow_star_dim.blp"

    d = c.get_by_id(166153)
    assert d is None
