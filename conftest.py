# flake8: noqa
import os


# deprecated hook, but it works
def pytest_cmdline_preparse(config, args):
    for i, arg in enumerate(args):
        if "@rootdir@" in arg:
            newpath = arg.replace("@rootdir@", str(config.rootdir))
            args[i] = os.path.normpath(newpath)
