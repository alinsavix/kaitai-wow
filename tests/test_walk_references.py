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


DATADIR = os.path.join("tests", "test_data")
OUTPUTDIR = os.path.join("tests", "outputs")
REFERENCEDIR = os.path.join("tests", "output_references")

# def test_command():
#     success, failmsg = capture_cmd("ls", ["-al"], outfile="out.txt", errfile="err.txt")
#     assert success, failmsg
# def test_test():
#     import wowdump
#     wowdump.main(["test_data/levelup.m2", "-o", "output/levelup.m2.txt"])
# def test_diff():
#     filediff("output_references/levelup.m2.txt", "output/levelup.m2.txt")
# @pytest.mark.tryfirst
# def test_wowdump():
#     # call and check help
#     pass
# lists of format examples to test
from collections import namedtuple
t = namedtuple("t", [ "file", "dumpflags" ])

tlist_tests = [
    t("8du_13495.wmo", []),
    t("8du_13495_000.wmo", []),
    t("8du_13495_000_lod1.wmo", []),

    t("diffuse_edgefade_t1_t2.bls", []),

    t("levelup.m2", []),
    t("levelup00.skin", ["--geometry"]),
    t("nightelfarcher_f.m2", []),
    t("nightelfarcher_f00.skin", []),
    t("nightelfarcher_f_lod01.skin", []),
    t("nightelffemale_hd0060-00.anim", []),
    t("flyingspriteevil.skel", []),
    # t("nightelffemale_hd_01.bone", []),
    t("nightelffemale_hd_markings_color_3641609.blp", []),

    t("spectraltiger.m2", []),
    t("staff_2h_draenorcrafted_d_02_c.m2", []),

    # t("zandalarcontinentfinale.tex", []),
    # t("zandalarcontinentfinale.wdl", []),
    t("zandalarcontinentfinale.wdt", []),
    # t("zandalarcontinentfinale_28_30.adt", []),
    # t("zandalarcontinentfinale_28_30_lod.adt", []),
    # t("zandalarcontinentfinale_28_30_obj0.adt", []),
    # t("zandalarcontinentfinale_28_30_obj1.adt", []),
    # t("zandalarcontinentfinale_28_30_tex0.adt", []),
    t("zandalarcontinentfinale_fogs.wdt", []),
    t("zandalarcontinentfinale_lgt.wdt", []),
    t("zandalarcontinentfinale_mpv.wdt", []),
    t("zandalarcontinentfinale_occ.wdt", []),
]


# generate the test list and such. Relatively simple, for now
def tlist():
    tests_list = []
    for test in tlist_tests:
        tests_list.append(pytest.param(test, id=test.file))

    return tests_list


# FIXME: should probably use a fixture-managed temp dir here, now
@pytest.fixture(scope="session")
def outputdir(request):
    outdir = os.path.join(request.config.rootdir, OUTPUTDIR, "walk")
    if os.path.exists(outdir):
        assert os.path.isdir(outdir), f"{outdir}: not a directory"
    else:
        os.makedirs(outdir)

    return outdir


@pytest.fixture(scope="module", params=tlist())
def t_output_walk(request, outputdir):
    test = request.param

    outpath = os.path.join(outputdir, f"{test.file}.txt")
    print(f"outputting tests to {outpath}")

    import wowdump
    wowdump.main([
        "--no-resolve",
        os.path.join(request.config.rootdir, DATADIR, test.file),
        "-o", outpath,
    ] + test.dumpflags)

    return test.file


def test_execute_walk(request, t_output_walk, extra):
    assert True


def test_diff_walk(request, t_output_walk, pytestconfig, extra):
    fn = t_output_walk

    refpath = os.path.join(request.config.rootdir, REFERENCEDIR, "walk", f"{fn}.txt")
    outpath = os.path.join(request.config.rootdir, OUTPUTDIR, "walk", f"{fn}.txt")

    assert util.filediff(refpath, outpath, limit=int(
        pytestconfig.getoption("diff_lines"))) == 0, "output file differences found"
