import os

import wowdump

DATADIR = os.path.join("tests", "test_data")
input_model = "levelup.m2"


# Make sure that arraylimit works for changing the array limit
def test_geometry_arraylimit(request, capsys, extra):
    ret = wowdump.main([
        "--no-resolve", "--geometry", "--arraylimit", "50",
        os.path.join(request.config.rootdir, DATADIR, input_model),

    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()

    # Make sure we don't get the elision message
    assert "geometry data elided, use --geometry to include" not in captured.out

    # verify we get geometry data up to our limit
    assert "/model/vertices/49" in captured.out

    # verify we don't get more than our limit
    assert "/model/vertices/50" not in captured.out

    # verify we get the elision message
    assert "/model/vertices/... = [50 elided of 100 total]" in captured.out


# Make sure that arraylimit doesn't limit when arraylimit=0
def test_geometry_arraylimit_zero(request, capsys, extra):
    ret = wowdump.main([
        "--no-resolve", "--geometry", "--arraylimit", "0",
        os.path.join(request.config.rootdir, DATADIR, input_model),
    ])
    assert ret == 0, f"wowdump exited with non-zero exit code ({ret})"

    captured = capsys.readouterr()

    # Make sure we don't get the geometry elision message (might be overkill)
    assert "geometry data elided, use --geometry to include" not in captured.out

    # verify we get all the geometry data (levelup.m2 has 100 verts, 0 - 99)
    assert "/model/vertices/99" in captured.out

    # verify we don't get an elision message at all
    assert "/model/vertices/..." not in captured.out
