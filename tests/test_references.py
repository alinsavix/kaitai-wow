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
from collections import namedtuple
t = namedtuple("t", ["infile", "type", "ext", "dumpflags"])

# lists of format examples to test
pathwalk_tests = [
    t("8du_13495.wmo", "walk", "txt", []),
    t("8du_13495_000.wmo", "walk", "txt", []),
    t("8du_13495_000_lod1.wmo", "walk", "txt", []),

    t("diffuse_edgefade_t1_t2.bls", "walk", "txt", []),

    t("levelup.m2", "walk", "txt", []),
    t("levelup00.skin", "walk", "txt", ["--geometry"]),
    t("nightelfarcher_f.m2", "walk", "txt", []),
    t("nightelfarcher_f00.skin", "walk", "txt", []),
    t("nightelfarcher_f_lod01.skin", "walk", "txt", []),
    t("nightelffemale_hd0060-00.anim", "walk", "txt", []),
    t("flyingspriteevil.skel", "walk", "txt", []),
    # t("nightelffemale_hd_01.bone", "walk", "txt",[]),
    t("nightelffemale_hd_markings_color_3641609.blp", "walk", "txt", []),

    t("spectraltiger.m2", "walk", "txt", []),
    t("staff_2h_draenorcrafted_d_02_c.m2", "walk", "txt", []),

    # t("zandalarcontinentfinale.tex", "walk", "txt", []),
    # t("zandalarcontinentfinale.wdl", "walk", "txt", []),
    t("zandalarcontinentfinale.wdt", "walk", "txt", []),
    # t("zandalarcontinentfinale_28_30.adt", "walk", "txt", []),
    # t("zandalarcontinentfinale_28_30_lod.adt", "walk", "txt", []),
    # t("zandalarcontinentfinale_28_30_obj0.adt", "walk", "txt", []),
    # t("zandalarcontinentfinale_28_30_obj1.adt", "walk", "txt", []),
    # t("zandalarcontinentfinale_28_30_tex0.adt", "walk", "txt", []),
    t("zandalarcontinentfinale_fogs.wdt", "walk", "txt", []),
    t("zandalarcontinentfinale_lgt.wdt", "walk", "txt", []),
    t("zandalarcontinentfinale_mpv.wdt", "walk", "txt", []),
    t("zandalarcontinentfinale_occ.wdt", "walk", "txt", []),
]

json_tests = [
    t("levelup00.skin", "json", "json", ["--output-type", "json"]),
]

all_tests = pathwalk_tests + json_tests


# generate the test list and such. Relatively simple, for now
def tlist():
    tests_list = []
    for test in all_tests:
        tests_list.append(pytest.param(test, id=f"{test.type}:{test.infile}"))

    return tests_list


# FIXME: should probably use a fixture-managed temp dir here, now
@pytest.fixture(scope="session")
def outputdir(request):
    outdir = os.path.join(request.config.rootdir, OUTPUTDIR)
    if os.path.exists(outdir):
        assert os.path.isdir(outdir), f"{outdir}: not a directory"
    else:
        os.makedirs(outdir)

    return outdir


@pytest.fixture(scope="module", params=tlist())
def t_reference_output(request, outputdir):
    test = request.param  # type: t

    outputsubdir = os.path.join(outputdir, test.type)
    if not os.path.exists(outputsubdir):
        os.makedirs(outputsubdir)

    inpath = os.path.join(request.config.rootdir, DATADIR, test.infile)
    outpath = os.path.join(outputsubdir, f"{test.infile}.{test.ext}")

    import wowdump
    wowdump.main([
        "--no-resolve",
        "-o", outpath,
    ] + test.dumpflags + [
        inpath,
    ])

    return test


def test_references(request, t_reference_output, extra):
    assert True


def test_diff_references(request, t_reference_output, pytestconfig, extra):
    test = t_reference_output  # type: t

    refpath = os.path.join(request.config.rootdir, REFERENCEDIR, test.type, f"{test.infile}.{test.ext}")
    outpath = os.path.join(request.config.rootdir, OUTPUTDIR, test.type, f"{test.infile}.{test.ext}")

    assert util.filediff(refpath, outpath, limit=int(
        pytestconfig.getoption("diff_lines"))) == 0, "output file differences found"
