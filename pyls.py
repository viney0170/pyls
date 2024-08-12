import argparse
import os
from datetime import datetime

# Setup command line argument parsing
parser = argparse.ArgumentParser(
    prog="pyls",
    description="Lists files in given or current directory",
    epilog="Poor man's ls",
)

parser.add_argument(
    "dirname",
    help="Name of directory to list the contents of",
    action="store",
    nargs="?",
    default=".",
)

parser.add_argument(
    "-l",
    "--long-format",
    help="Presents more details about files in columnar format",
    action="store_true",
)

parser.add_argument(
    "-F",
    "--filetype",
    help="Adds an extra character to the end of the printed filename that indicates its type.",
    action="store_true",
)

args = parser.parse_args()