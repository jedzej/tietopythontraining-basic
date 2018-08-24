#! python3
"""
Walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.

Usage
-----
$ py selcopy0.pyw <ext> <source_folder> <target_folder>

Examples
--------
$ py selcopy0.pyw txt samples copies

$ py selcopy0.pyw txt samples ..\copies
"""

import shutil, os, sys

ext = sys.argv[1]
source_folder = os.path.abspath(sys.argv[2])
target_folder = os.path.abspath(sys.argv[3])

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for folder, subfolders, files in os.walk(source_folder):

    for file in files:

        if file.endswith(ext):
            file_path = os.path.join(folder, file)

            shutil.copy(file_path, target_folder)
            print("File {} copied.".format(file_path))
