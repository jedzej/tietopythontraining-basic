"""
Write a program that walks through a folder tree and
searches for files with a certain file extension
(such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

import os
import re
import shutil


def find_and_copy(extension, src, dst):
    copy_dir = os.path.join(os.getcwd(), dst)
    if not os.path.exists(copy_dir):
        os.makedirs(copy_dir)

    pattern = re.compile("^.*\." + extension)
    for folderName, subfolders, filenames in os.walk(src):
        for file in filenames:
            if pattern.match(file):
                path = os.path.join(folderName, file)
                shutil.copy(path, copy_dir)


def main():
    find_and_copy("mp4",  os.getcwd() + "/selective_copy_dir", os.getcwd() + "/new_folder")


if __name__ == '__main__':
    main()
