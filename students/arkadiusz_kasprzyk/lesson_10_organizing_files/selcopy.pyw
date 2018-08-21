#! python3
"""
Walks through a folder tree and searches for files
with names satisfying given standard Unix pattern
(passed with the use of wildcards '*', '?', etc.).
Copy these files from whatever location they are into a new folder.

Usage
-----
$ py selcopy.pyw <source_files> <target_folder>

Examples
--------
$ python selcopy.pyw samples\*.txt copies

$ python selcopy.pyw samples\*.txt ..\copies

$ python selcopy.pyw samples\samp* copies
"""

import shutil, os, sys, glob

source = sys.argv[1]

source_folder, source_files = os.path.split(source)

source_folder = os.path.abspath(source_folder)

target_folder = os.path.abspath(sys.argv[2])

if not os.path.exists(target_folder):
    os.makedirs(target_folder)


def new_file_name(file_name):
    k = 2
    name, ext = file_name.rsplit(".", 1)

    file_name = "{} ({}).{}".format(name, k, ext)

    while os.path.exists(file_name):
        k += 1
        file_name = "{} ({}).{}".format(name, k, ext)

    return file_name


# log file
logfile_name = os.path.join(target_folder, "logfile.txt")
if os.path.exists(logfile_name):
    logfile_name = new_file_name(logfile_name)

logfile = open(logfile_name, "w")
logfile.writelines("Copying {} recursively from tree rooted in ". \
                   format(source_files) +
                   "\n{}\nto".format(source_folder) +
                   "\n{}\n\n".format(target_folder))


for folder, subfolders, files in os.walk(source_folder):
    # we use only `folder` -- this is absolute path

    if folder == target_folder:
        # we do not copy from the target folder
        continue

    for source_file in glob.glob(os.path.join(folder, source_files)):
        # uses standard Unix pattern
        # here returns absolute path

        file = os.path.split(source_file)[1]

        target_file = os.path.join(target_folder, file)

        source_file_rel = os.path.relpath(path=source_file,
                                          start=source_folder)

        if os.path.exists(target_file):

            target_file = new_file_name(target_file)

            target_file_rel = os.path.relpath(path=target_file,
                                              start=target_folder)

            message = "copied: {}\n    to: {}\n".format(source_file_rel,
                                                        target_file_rel)

        else:

            message = "copied: {}\n".format(source_file_rel)

        shutil.copy(source_file, target_file)
        logfile.writelines(message)
        print(message)

logfile.close()
