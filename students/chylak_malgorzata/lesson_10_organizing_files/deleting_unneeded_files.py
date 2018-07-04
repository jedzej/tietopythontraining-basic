#! python 3
# deleting_unneeded_files walks through a folder tree and searches for
# files larger than 100MB and prints their absolute path to the screen.

import os


def large_files(folder):
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            file_size = os.path.getsize(foldername + '\\' + filename)
            if int(file_size) < 1000000:
                continue
            print(filename)


large_files('C:\Folder')
print('Done')
