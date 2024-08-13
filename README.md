# pyls

`pyls` is a Python-based command-line utility that mimics basic functionalities of the traditional UNIX `ls` command. It allows users to list directory contents with options to display detailed file information and file type indicators.

## Features

- List files and directories in the specified or current directory.
- Optionally display detailed information about files (`-l` flag), including last modified time and size.
- Optionally append a character to each filename to indicate its type (`-F` flag):
  - `/` for directories
  - `*` for executable files

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/pyls.git
cd pyls
