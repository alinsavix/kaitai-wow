import os
import random

import pytest

import wowdump
import wowdump.filetypes

DATADIR = os.path.join("tests", "test_data")

# kind of a hack, because pytest makes it difficult to pass via the
# command line in a useful way. See the comments in conftest.py
BULKDIR = os.getenv("TEST_BULKDIR")
BULKCOUNT = os.getenv("TEST_BULKCOUNT")
BULKSEED = os.getenv("TEST_BULKSEED")

# generate the test list and such
def t_bulk_list(bulkdir=BULKDIR, bulkcount=BULKCOUNT, bulkseed=BULKSEED):
    # This makes me feel dirty, but if we intentionally have no bulk tests,
    # return a canary value that we'll check for later, so that these tests
    # show up as passed, rather than skipped.
    #
    # FIXME: Is there a better way?
    if bulkdir is None:
        return [pytest.param("no_bulk_tests", id="no_bulk_tests")]

    supported = wowdump.filetypes.get_supported()

    # FIXME: Skip this list generation and randomization in the case of
    # bulkcount = 0?
    possible_tests = []
    for dirpath, _dirs, files in os.walk(bulkdir):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext[1:].lower()
            if ext in supported:
                possible_tests.append(pytest.param(os.path.join(dirpath, file), id=file))

    # Should we fail instead of just not doing tests, if someone specifies a
    # bulkdir but no files are valid types?
    if len(possible_tests) == 0:
        return [pytest.param("no_bulk_tests", id="no_bulk_tests")]

    # If we didn't specify a bulkcount, return everything
    if not bulkcount:
        return possible_tests



    # otherwise, pick a random set of tests
    if bulkseed:
        bulkseed = int(bulkseed)
    random.seed(bulkseed)
    return random.sample(possible_tests, int(bulkcount))


@pytest.fixture(params=t_bulk_list())
def t_bulk(request, extra):
    fn = request.param  # type: str

    if fn == "no_bulk_tests":
        return

    ret = wowdump.main([
        "--no-resolve",
        "-o", "scratch.txt",
        fn,
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    return fn

@pytest.mark.order(-1)
def test_bulk(t_bulk, extra):
    assert True
