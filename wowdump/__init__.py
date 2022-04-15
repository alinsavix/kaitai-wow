# flake8: noqa
# type: ignore

try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'unknown'

# FIXME: the listfile stuff here is painful
from .wowdump import get_default_listfile, main, set_default_listfile
