#!/usr/bin/env python3

"""
deleting_unneeded_files.py: a practice project "Deleting Unneeded Files" from:
https://automatetheboringstuff.com/chapter9/

The program walks through a folder tree and searches for exceptionally large
files or folders (size > 100 MB).

Usage: ./deleting_unneeded_files.py <folder_path>

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os


BYTES_IN_MEGABYTE = 1024 * 1024
FILE_SIZE_MAX = 100 * BYTES_IN_MEGABYTE


def get_args():

    args_cnt = len(sys.argv)

    if args_cnt != 2:
        print('Usage: ./deleting_unneeded_files.py <path>')
        return None

    else:
        path = sys.argv[1]

        if not os.path.exists(path) or not os.path.isdir(path):
            print("Error! The path: {} is incorrect!".format(path))
            return None

        return path


def main():

    path = get_args()
    if path is not None:

        for curr_dir, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(curr_dir, file)
                size_in_bytes = os.path.getsize(file_path)
                if FILE_SIZE_MAX < size_in_bytes:
                    print('File: {}, size: {} MB'.format(file_path,
                                                         size_in_bytes /
                                                         BYTES_IN_MEGABYTE))


if __name__ == '__main__':
    main()
