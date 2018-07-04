#!/usr/bin/env python3

"""
selective_copy.py: a practice project "Selective Copy" from:
https://automatetheboringstuff.com/chapter9/

The program walks through a folder tree and searches for files with a given
file extension. Then it copies these files from the source location to
a destination folder.

Usage: ./selective_copy.py <extension> <source_path> <destination_path>

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os
import shutil
import random


def get_args():

    args_cnt = len(sys.argv)

    if args_cnt != 4:
        print("Usage: ./selective_copy.py <extension> <source_path> "
              "<destination_path>")
        return None

    else:
        extension, source, destination = sys.argv[1:]
        if not extension:
            print('Error! The extension cannot be an empty string!')
            return None

        if not os.path.exists(source) or not os.path.isdir(source):
            print("Error! The source path: {} is incorrect!".format(source))
            return None

        if not os.path.exists(destination):
            os.makedirs(destination)
        elif not os.path.isdir(destination):
            print('Error! The destination path leads to a file')
            return None

        if not os.path.isabs(destination):
            destination = os.path.abspath(destination)

        return extension, source, destination


def main():

    args = get_args()
    if args is not None:
        extension, source, destination = args

        for curr_dir, _, files in os.walk(source):
            for file in files:
                if file.endswith('.{}'.format(extension)):
                    if os.path.exists(os.path.join(destination, file)):
                        name, ext = os.path.splitext(file)

                        new_name = '{}_{}_{}'.format(name,
                                                     random.randint(1, 999999),
                                                     ext)
                        shutil.copy(os.path.join(curr_dir, file),
                                    os.path.join(destination, new_name))
                        print('File names collision; renaming file {} copied '
                              'from: {} to {}'.format(file, curr_dir, new_name)
                              )
                    else:
                        shutil.copy(os.path.join(curr_dir, file), destination)


if __name__ == '__main__':
    main()
