#! python3
"""
Creates series of (empty) text files with given prefix,
numbering and extension, all read off from one string.
Does not overwrite already existing files.

Usage
-----
$ py makefiles.pyw <folder\prefixRange.ext>

Example
-------
$ py mekefiles.pyw spam008.txt
will create files spam001.txt, ..., spam008.tx
in working directory

$ py mekefiles.pyw folder\spam008.txt
the same in the given folder

Remarks
-------
RegExp seems to be necessary to do it neatly.
"""

import os, sys, re

full_path = sys.argv[1]

folder, file = os.path.split(full_path)

if folder == '':
    folder = os.getcwd()
else:
    folder = os.path.abspath(folder)

os.chdir(folder)

name, ext = file.rsplit('.', 1)

prefix = name.rstrip('0123456789')

regex = re.compile(r'[0-9]+$')

try:
    numbering = regex.search(name).group()
except AttributeError:
    numbering = '1'

num_width = len(numbering)

numbering = numbering.lstrip('0')
if numbering == '':
    numbering = '1'

num_max = int(numbering)

def file_new(k):
    num = str(k).zfill(num_width)
    return "{}{}.{}".format(prefix, num, ext)

for n in range(1, num_max + 1):
    fn = file_new(n)
    if not os.path.exists(fn):
        f = open(os.path.join(folder, fn), 'a')
        f.close()
        print("File {} created.".format(fn))
    else:
        print("File {} already exists.".format(fn))
