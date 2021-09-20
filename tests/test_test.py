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

DATADIR = os.path.join(".", "test_data")
OUTPUTDIR = os.path.join(".", "outputs")
REFERENCEDIR = os.path.join(".", "output_references")

# Other args to consider: --ignore-case,  --ignore-all-space
def filediff(reference: os.PathLike, testfile: os.PathLike,
             limit: int = 200):
    exe = "diff"
    args = [
        "--unified=0", "--minimal", "--speed-large-files", "--text",
        "--label", "LABEL", "--label", "LABEL",  # no intro lines
        str(reference), str(testfile)
    ]
    # print(f"Executing command: {exe}", str.join(" ", args))
    # print(f"current dir is: {os.getcwd()}")
    # result = subprocess.run([exe] + args, stdin=None, check=True)
    with subprocess.Popen([exe] + args, universal_newlines=True, bufsize=1,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          stdin=subprocess.DEVNULL,
                          ) as proc:
        linecount = 0
        line = proc.stdout.readline()
        while line and (linecount < limit):
            linecount += 1
            print(line, end="")
            line = proc.stdout.readline()

        # if we're here we either ran out of lines, or got too many lines
        # consume any extra lines
        extra = 0
        while line:
            extra += 1
            line = proc.stdout.readline()


        if extra > 0:
            print(f"WARNING: too many line differences, {extra} lines hidden")

        # hopefully diff is done, reap it
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()

        return proc.returncode


# below from previous subprocess w/ output capture thing
    # success = True
    # failmsg = None
    # with open(outfile, "w") as stdout, open(errfile, "w") as stderr:
    #     try:
    #         os.environ['PYTHONUNBUFFERED'] = "1"
    #         result = subprocess.run([exe] + args, stdin=None, stdout=stdout,
    #                                 stderr=stderr, timeout=timeout, check=True)
    #     except (subprocess.CalledProcessError) as e:
    #         t = type(e).__name__
    #         success = False
    #         failmsg = f"{exe} process failed ({t}), exit code: {e.returncode}"
    #     except (OSError) as e:
    #         t = type(e).__name__
    #         success = False
    #         failmsg = f"error executing {exe}: {t} - {e}"
    # return success, failmsg
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
tlist_tests = [
    "8du_13495.wmo",
    "8du_13495_000.wmo",
    "8du_13495_000_lod1.wmo",
    "diffuse_edgefade_t1_t2.bls",
    "levelup.m2",
    "levelup00.skin",
    # "nightelfarcher_f.m2",
    # "nightelfarcher_f.skel",
    # "nightelfarcher_f00.skin",
    # "nightelfarcher_f_lod01.skin",
    # "nightelffemale_hd.m2",
    # "nightelffemale_hd.skel",
    # "nightelffemale_hd00.skin",
    # "nightelffemale_hd0060-00.anim",
    # "nightelffemale_hd_01.bone",
    # "nightelffemale_hd_markings_color_3641609.blp",
    # "spectraltiger.m2",
    # "staff_2h_draenorcrafted_d_02_c.m2",
    # "zandalarcontinentfinale.tex",
    # "zandalarcontinentfinale.wdl",
    # "zandalarcontinentfinale.wdt",
    # "zandalarcontinentfinale_28_30.adt",
    # "zandalarcontinentfinale_28_30_lod.adt",
    # "zandalarcontinentfinale_28_30_obj0.adt",
    # "zandalarcontinentfinale_28_30_obj1.adt",
    # "zandalarcontinentfinale_28_30_tex0.adt",
    # "zandalarcontinentfinale_fogs.wdt",
    # "zandalarcontinentfinale_lgt.wdt",
    # "zandalarcontinentfinale_mpv.wdt",
    # "zandalarcontinentfinale_occ.wdt",
]

# generate the test list and such. Relatively simple, for now
def tlist():
    tests_list = []
    for test in tlist_tests:
        tests_list.append(pytest.param(test, id=test))

    return tests_list


@pytest.fixture(scope="module", params=tlist())
def t_output_walk(request):
    fn = request.param

    outpath = os.path.join(OUTPUTDIR, "walk", f"{fn}.txt")

    import wowdump
    wowdump.main([
        "--no-resolve",
        os.path.join(DATADIR, fn),
        "-o", outpath,
    ])

    return fn


def test_execute_walk(t_output_walk, extra):
    assert True


def test_diff_walk(t_output_walk, extra):
    fn = t_output_walk

    refpath = os.path.join(REFERENCEDIR, "walk", f"{fn}.txt")
    outpath = os.path.join(OUTPUTDIR, "walk", f"{fn}.txt")

    assert filediff(refpath, outpath) == 0, "output differences found"
