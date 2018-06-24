"""
Write a program that walks through a folder tree and
searches for files with a certain file extension
(such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

import argparse
import os
import re
import shutil
import sys


def args_parameters(args):
    parser = argparse.ArgumentParser(
        description='Copy only specific file format:')
    parser.add_argument('-e', '--extension',
                        help="extension of the files to copy", required=True)
    parser.add_argument('-s', '--source', help="source directory",
                        default=os.getcwd() + "/selective_copy_dir")
    parser.add_argument('-d', '--destination', help="destination directory",
                        default=os.getcwd() + "/selective_copies")

    result = parser.parse_args()

    return result.extension, result.source, result.destination


extension, source, destination = args_parameters(sys.argv)


def find_and_copy(ext, src, dst):
    copy_dir = os.path.join(os.getcwd(), dst)
    if not os.path.exists(copy_dir):
        os.makedirs(copy_dir)

    pattern = re.compile("^.*\." + ext)
    for folderName, subfolders, filenames in os.walk(src):
        for file in filenames:
            if pattern.match(file):
                path = os.path.join(folderName, file)
                shutil.copy(path, copy_dir)


def main():
    find_and_copy(extension, source, destination)


if __name__ == '__main__':
    main()
