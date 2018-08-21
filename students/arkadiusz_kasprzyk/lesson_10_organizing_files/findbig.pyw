#! python3
"""
Walks through a folder tree and searches for
exceptionally large files or folders, e.g.
ones that have a file size of more than 100MB.
Prints these files with their absolute folder to the screen.

Usage
-----
$ py findbig.pyw <size in MB> <top_folder>

Example
-------
$ py findbig.pyw 100 ..
"""

import os, sys

min_size = int(sys.argv[1]) * 1024 * 1024  # MB
top = os.path.abspath(sys.argv[2])

for folder, subfolders, files in os.walk(top):

    for file in files:
        file_path = os.path.join(folder, file)
        file_size = os.path.getsize(file_path)
        if file_size > min_size:
            print("The file {} has size of {:.3f} MB."
                  .format(file_path, file_size / 1024 / 1024))
