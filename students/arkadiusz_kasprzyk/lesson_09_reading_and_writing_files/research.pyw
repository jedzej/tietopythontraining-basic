#! python3
"""
Usage
-----
$ py research.pyw <reg_exp>
$ py research.pyw <reg_exp> <folder>

Examples
--------
$ py research.pyw "^[a-z]"
$ py research.pyw ^^[a-z]
$ py research.pyw "^[A-Z !.]$"
$ py research.pyw \.$

$ py research.pyw ^^[a-z] ./sampletexts
$ py research.pyw ^^[A-Z] ./sampletexts
$ py research.pyw ^^\s+ ./sampletexts
$ py research.pyw import ./sampletexts
$ py research.pyw \.$ ./sampletexts

Remarks
-------
Use double quotes for regexp: "regexp" when it contains a raw space.
If " is not used then ^ at the beginning must be doubled.
"""

import sys, os
import re

reg = re.compile(sys.argv[1].strip("\""))

if len(sys.argv) > 2:
    path = sys.argv[2]
else:
    path = os.getcwd()

files = os.listdir(path)
files = [f for f in files if re.search(r'\.txt$',f)]

for f in files:
    print("\t" + f)
    f = open(os.path.join(path, f), 'r')
    for line in f:
        # print(line.strip("\n"))
        if reg.search(line):
            print(line.strip("\n"))
        # else:
        #     print('0')
    print()
