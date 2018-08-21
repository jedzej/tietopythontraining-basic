#! python3
"""
Finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Renames all the later files to close this gap.

Usage
-----
$ py fillgaps.pyw <[folder\]prefix.ext>

Example
-------
$ py fillgaps.pyw spam.txt

$ py fillgaps.pyw samples\spam.txt

Assumptions
-----------
1. We deal with files of one type (by extension) at a time.
2. File names consists only of prefix and number i.e. prefix001.ext, ...
3. Numbering should start with 1.
4. Padding with 0's do not have to be consistent,
   but final numbering will be padded with 0's to the common length
   (maximum of original "numbers" length).
"""

import os, sys


file_path = sys.argv[1]

path, file = os.path.split(file_path)

if path == '':
    path = os.getcwd()
else:
    path = os.path.abspath(path)

prefix, ext = file.rsplit(".", 1)

# files with given prefix and extension
files = [file for file in os.listdir(path)
         if file.endswith(ext) and file.startswith(prefix)]

if len(files) == 0:
    sys.exit("The file list is empty.")

# files and theirs "numbers"
files = [(file, file.rpartition(".")[0].replace(prefix, "", 1))
         for file in files]

# only files whose "numbers" are really numbers
files = [file for file in files if file[1].isnumeric()]

if len(files) == 0:
    sys.exit("The file list is empty.")

# numbering width
width = max([len(file[1]) for file in files])


def file_new(k):
    num = str(k).zfill(width)
    return "{}{}.{}".format(prefix, num, ext)


files = [(file[0], file_new(k + 1)) for k, file in enumerate(files)]

for file, file_new in files:
    if file != file_new:
        print(file, '->', file_new)
        os.rename(os.path.join(path, file),
                  os.path.join(path, file_new))
