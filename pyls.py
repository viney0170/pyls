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

def main(args) :
    results = get_descriptions_of_files_in_dir(args.dirname, args.long_format, args.filetype)
    lines = format_results(results, args.long_format, args.filetype)
    display_results(lines)

def get_descriptions_of_files_in_dir(dirname, long_format, filetype):
    """
    Lists the files and folders in the given directory
    and constructs a list of dicts with the required information.

    Args:
    dirname (str): The directory whose contents are to be listed.
    long_format (bool): True if the user has asked for the long format.
    filetype (bool): True if the user has asked for file type info as well.

    Returns:
    list: A list of dictionaries each with keys - filename, filetype, modtime, filesize.
    """
    entries = os.listdir(dirname)
    descriptions = []
    for entry in entries:
        full_path = os.path.join(dirname, entry)
        modtime = datetime.fromtimestamp(os.path.getmtime(full_path))
        filesize = os.path.getsize(full_path) if not os.path.isdir(full_path) else 0
        file_type = 'd' if os.path.isdir(full_path) else 'x' if os.access(full_path, os.X_OK) else 'f'
        descriptions.append({
            "filename": entry,
            "filetype": file_type,
            "modtime": modtime,
            "filesize": filesize,
        })
    return descriptions

def format_results(results, long_format, filetype):
    """
    Formats a list of file descriptions for display.

    Args:
    results (list): List of dictionaries like returned by get_descriptions_of_files_in_dir().
    long_format (bool): Boolean that indicates long format output.
    filetype (bool): Boolean that indicates ask for extra type descriptor character at end.

    Returns:
    list: A list of formatted strings.
    """
    
    lines = []
    for result in results:
        if long_format:
            line = f"{result['modtime'].strftime('%Y-%m-%d %H:%M:%S')} {result['filesize']:>6} {result['filename']}"
        else:
            line = result['filename']
        if filetype:
            if result['filetype'] == 'd':
                line += '/'
            elif result['filetype'] == 'x':
                line += '*'
        lines.append(line)
    return lines


def display_results(lines):
    for line in lines: 
        print(line)

if __name__ == "__main__":
    main(args)
