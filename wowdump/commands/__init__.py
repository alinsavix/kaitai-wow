# flake8: noqa
import argparse
from typing import Callable

from .bulkwalk import cmd_bulkwalk
from .pathwalk import cmd_pathwalk
from .simple import cmd_final, cmd_json, cmd_raw, cmd_report

WowdumpCommand = Callable[[argparse.Namespace], int]
