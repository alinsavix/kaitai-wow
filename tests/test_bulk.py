import collections
import csv
import os
import posixpath
import pprint
import re
import subprocess
import sys

from typing import List

import pytest
from pytest_html import extras

from testutil import util
import wowdump

DATADIR = os.path.join("tests", "test_data")

# kind of a hack, because pytest makes it difficult to pass via the
# command line in a useful way. Just set this env var to something to
# actually run bulk tests as a one-off.
BULKDIR = os.getenv("TEST_BULKDIR")

@pytest.fixture
def bulkdir():
    return BULKDIR

# generate the test list and such. Relatively simple, for now
def t_bulk_list(bulkdir=BULKDIR):
    tests_list = []

    # This makes me feel dirty, but if we intentionally have no bulk tests,
    # return a canary value that we'll check for later, so that these tests
    # show up as passed, rather than skipped.
    #
    # FIXME: Is there a better way?
    if bulkdir is None:
        tests_list.append(pytest.param("no_bulk_tests", id="no_bulk_tests"))
        return tests_list

    for dirpath, _dirs, files in os.walk(bulkdir):
        for file in files:
            tests_list.append(pytest.param(os.path.join(bulkdir, dirpath, file), id=file))

    return tests_list

@pytest.fixture(params=t_bulk_list())
def t_bulk(request, bulkdir, extra):
    fn = request.param  # type: str

    if fn == "no_bulk_tests":
        return

    ret = wowdump.main([
        "--no-resolve",
        "-o", "scratch.txt",
        os.path.join(BULKDIR, fn),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    return fn

@pytest.mark.order(-1)
def test_bulk(t_bulk, extra):
    assert True
