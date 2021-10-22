import argparse
import os


# This kinda sucks -- there's not really a good/simple way (that I can find)
# to pass command-line arguments to the test collectors (which don't accept
# fixtures as arguments), but we need that to be able to do our one-off 'bulk'
# tests. So we're going to set things in the environment when we get them as
# options. I guess I could also set something in the module namespace? It's
# a hack any way you cut it, and it sucks.
class SetBulkEnvFromOptions(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, values)
        if option == "--bulkdir":
            os.environ["TEST_BULKDIR"] = str(values)
        elif option == "--bulkcount":
            os.environ["TEST_BULKCOUNT"] = str(values)
        elif option == "--bulkseed":
            os.environ["TEST_BULKSEED"] = str(values)


def pytest_addoption(parser):
    parser.addoption(
        "--diff-lines",
        action='store',
        default=200,
    )

    # We're not actually going to use bulkdir arguments, we're just going to
    # use the action to set some environment variables
    parser.addoption(
        "--bulkdir",
        type=str,
        action=SetBulkEnvFromOptions,
        default=None,
    )

    parser.addoption(
        "--bulkcount",
        type=int,
        action=SetBulkEnvFromOptions,
        default=None,
    )

    parser.addoption(
        "--bulkseed",
        type=int,
        action=SetBulkEnvFromOptions,
        default=None,
    )
