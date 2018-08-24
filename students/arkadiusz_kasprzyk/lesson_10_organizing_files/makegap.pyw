#! python3
"""
Finds all files with a given prefix and extension,
such as spam001.txt, spam002.txt, and so on,
in a single folder and renames files to create a gap in numbering.

Usage
-----
$ py makegap.pyw <[folder\]prefix.ext> <gap_end> [<gap_start>]

Example
-------
$py makegap.pyw samples\spam.txt 5 3
makes gap in numbering extending from 3 to 5 (including!), e.g.
series
spam01.txt, spam02.txt, spam03.txt, spam04.txt
will be turned to
spam01.txt, spam02.txt, spam06.txt, spam07.txt

$py makegap.pyw samples\spam.txt 5 5
makes gap in numbering only at 5 (including!)
the same as:

$py makegap.pyw samples\spam.txt 5

$py makegap.pyw samples\spam.txt 005
makes gap at 5 and pads all numbering to length 3

$ py makegap.pyw samples\spam.txt 1
moves all the numbering by 1 (except files with names ending with 0)

$ py makegap.pyw samples\spam.txt 3 1
moves all the numbering by 3 (except files with names ending with 0)

$ py makegap.pyw samples\spam.txt 3 0
moves all the numbering by 3 (also files with names ending with 0)

$ py makegap.pyw samples\spam.txt 3
makes gap at 3

An interesting side effect is widening padding for all files:
$ py makegap.pyw samples\spam.txt 000
will result with numbering length of 3 signs for all files
with numbers unchanged if only spam.00 doesn't exist (it shouldn't!)

Assumptions
-----------
1. We deal with files of one type (by extension) at a time.
2. File names consists only of prefix and number i.e. prefix001.ext, ...
3. Numbering should start with 1.
4. Padding with 0's do not have to be consistent,
   but final numbering for the files renamed will be padded with 0's
   to the common length (maximum of original "numbers" length).
5. Generally: inconsistent padding is treated as mistake
   thus in one folder there should NOT be two series of files
   having only different padding;
   in such a case FileExistsError may appear during files renaming.
"""

import os, sys

full_path = sys.argv[1]

path, file = os.path.split(full_path)

if path == '':
    path = os.getcwd()
else:
    path = os.path.abspath(path)

os.chdir(path)

prefix, ext = file.rsplit(".", 1)


gap_end = sys.argv[2]

if len(sys.argv) > 3:
    gap_start = sys.argv[3]
else:
    gap_start = gap_end

width = max(len(gap_end), len(gap_start))

gap_end, gap_start = int(gap_end), int(gap_start)

#if gap_end < 1:
#    sys.exit("The second parameter `gap_end` cannot be 0.")

if gap_end < gap_start:
    sys.exit("The third parameter (`gap_start`) " +
             "cannot be greater than the second (`gap_end`)\n" +
             "it is optional, and its default value is `gap_end`."
            )

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
width = max(width, max([len(file[1]) for file in files]))

# files and theirs "real" numbers
files = [(file[0], int(file[1])) for file in files]


def file_new(k):
    num = str(k).zfill(width)
    return "{}{}.{}".format(prefix, num, ext)


files_lower = [(file, k) for file, k in files if k < gap_start]
files_upper = list(set(files).difference(files_lower))

min_upper = min([k for file, k in files_upper])
shift = max(0, gap_end + 1 - min_upper)

files_lower = [(file, file_new(k)) for file, k in files_lower]
files_upper = \
    [(file, file_new(k + shift)) for file, k in files_upper]

files = files_lower + files_upper

files.sort(key=lambda f: f[1], reverse=True)

for file, file_new in files:
    if file != file_new:
        try:
            print(file, '->', file_new)
            os.rename(os.path.join(path, file),
                      os.path.join(path, file_new))
        except FileExistsError:
            # it may happen only in case of two file series
            # with different padding
            print("Cannot rename {} to {}\n".format(file, file_new),
                  "- file already exists.")
