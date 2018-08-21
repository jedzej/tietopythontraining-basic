#! python3
"""
Finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Renames all the later files to close this gap.

Usage
-----
$ py fillgaps0.pyw <prefix> [<ext> [<path>]]

Example
-------
$ py fillgaps0.pyw spam txt

Remarks
-------
1. Assume that we deal with files of one type (by extension) at a time.
2. File names consist only of prefix and number i.e. prefix001.ext, ...
3. Numbering should start with 1.
"""

import os, sys, shutil

prefix = sys.argv[1]

ext = sys.argv[2]

if len(sys.argv) > 3:
    path = sys.argv[3]
else:
    path = os.getcwd()

MESSAGE = "The file list is empty."

# files with given extension
files = [file for file in os.listdir(path) if file.endswith(ext)]

try:
    # files and theirs "numbers"
    files = [(file, file.rpartition(".")[0].replace(prefix, "", 1))
             for file in files]
except:
    print(MESSAGE)

    # numbering width
    width = len(files[0][1])

# only files whose "numbers" are really numbers
files = [file for file, num in files if num.lstrip("0").isnumeric()]

try:
    def file_new(k):
        num = str(k).zfill(width)
        return "{}{}.{}".format(prefix, num, ext)

    files = [(file, file_new(k)) for k in range(len(files))]

    for file, file_new in files:
        os.rename(file, file_new)
except:
    print(MESSAGE)
