import os

def pytest_addoption(parser):
    parser.addoption(
        "--diff-lines",
        action='store',
        default=200,
    )


# deprecated hook
def pytest_cmdline_preparse(config, args):
    for i, arg in enumerate(args):
        if "@rootdir@" in arg:
            newpath = arg.replace("@rootdir@", str(config.rootdir))
            args[i] = os.path.normpath(newpath)
