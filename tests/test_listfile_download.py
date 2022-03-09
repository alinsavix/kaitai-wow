# type: ignore
import logging

import wowdump

import pytest
# import requests
import responses

# FIXME: Not sure why I can't pull this in from main wowdump
DEFAULT_LISTFILE_URL: str = "https://github.com/wowdev/wow-listfile/raw/master/community-listfile.csv"

@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps

def test_download_200(tmp_path, mocked_responses, capsys, extra):
    mocked_responses.add(
        responses.GET, DEFAULT_LISTFILE_URL,
        body='12345;DEFAULT_LISTFILE_URL DOWNLOAD', status=200,
        content_type='application/json')

    listfile = tmp_path / "listfile.csv"
    ret = wowdump.main([
        "--listfile", str(listfile),
        "--download-listfile",
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
    assert listfile.read_text() == "12345;DEFAULT_LISTFILE_URL DOWNLOAD"


def test_download_404(tmp_path, mocked_responses, capsys, extra):
    mocked_responses.add(
        responses.GET, DEFAULT_LISTFILE_URL,
        body='DEFAULT_LISTFILE_URL ERROR', status=404)

    listfile = tmp_path / "listfile.csv"
    ret = wowdump.main([
        "--listfile", str(listfile),
        "--download-listfile",
    ])
    assert ret == 69, f"wowdump exited with improper exit code (should be 69 (os.EX_UNAVAILABLE)), was {ret}"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
    assert "ERROR: couldn't download listfile: 404 Not Found" in captured.err


def test_download_500(tmp_path, mocked_responses, capsys, extra):
    mocked_responses.add(
        responses.GET, DEFAULT_LISTFILE_URL,
        body='DEFAULT_LISTFILE_URL ERROR', status=500)

    listfile = tmp_path / "listfile.csv"
    ret = wowdump.main([
        "--listfile", str(listfile),
        "--download-listfile",
    ])
    assert ret == 69, f"wowdump exited with improper exit code (should be 69 (os.EX_UNAVAILABLE)), was {ret}"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
    assert "ERROR: couldn't download listfile: 500 Internal Server Error" in captured.err


def test_download_alternate_url(tmp_path, mocked_responses, capsys, extra):
    alternate_url = "http://example.com/listfile.csv"
    mocked_responses.add(
        responses.GET, alternate_url,
        body='12345;ALTERNATE_URL DOWNLOAD', status=200)

    listfile = tmp_path / "listfile.csv"
    ret = wowdump.main([
        "--listfile", str(listfile),
        "--listfile-url", alternate_url,
        "--download-listfile",
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
    assert listfile.read_text() == "12345;ALTERNATE_URL DOWNLOAD"


# test the behavior of --download-listfile when the listfile is and
# isn't present
def test_download_force_flag(tmp_path, mocked_responses, capsys, caplog, extra):
    mocked_responses.add(
        responses.GET, DEFAULT_LISTFILE_URL,
        body='12345;DEFAULT_LISTFILE_URL DOWNLOAD', status=200,
        content_type='application/json')

    listfile = tmp_path / "listfile.csv"
    wowdump.set_default_listfile(listfile)

    # If it doesn't exist and we've said we don't want to download it,
    # make sure we don't download it
    assert not listfile.exists(), "our fresh tmpdir already has a listfile?!"
    ret = wowdump.main([
        # "--listfile", str(listfile),
        "--no-download-listfile",
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    # assert ("csvcache", logging.WARNING,
    #         str(listfile) + " does not exist, not resolving fileids") in caplog.record_tuples
    captured = capsys.readouterr()
    assert "WARNING: listfile does not exist, fdid name resolution disabled" in captured.err
    assert not listfile.exists(), "downloaded listfile when we shouldn't have"


    # If it doesn't exist otherwise, we should try to download it
    ret = wowdump.main([
        # "--listfile", str(listfile),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
    assert listfile.read_text() == "12345;DEFAULT_LISTFILE_URL DOWNLOAD"


    # it exists now, make sure we don't try to download it again
    # If it doesn't exist otherwise, we should try to download it
    ret = wowdump.main([
        # "--listfile", str(listfile),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()
    assert "WARNING: listfile does not exist" not in captured.err
    assert "NOTICE: downloading new listfile" not in captured.err


    # it exists, but make sure we _do_ try to download it if we
    # explicitly request it
    ret = wowdump.main([
        # "--listfile", str(listfile),
        "--download-listfile",
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()
    assert "NOTICE: downloading new listfile" in captured.err
