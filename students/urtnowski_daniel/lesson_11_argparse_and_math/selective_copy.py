#!/usr/bin/env python3

"""
selective_copy.py: a practice project "Selective Copy" from:
https://automatetheboringstuff.com/chapter9/

The program walks through a folder tree and searches for files with a given
file extension. Then it copies these files from the source location to
a destination folder.

Usage: selective_copy.py [-h] -e EXTENSION [-s SRC] -d DST

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os
import shutil
import random
import argparse
import helpers


def get_args():
    parser = argparse.ArgumentParser(
        description='The program walks through a folder tree and searches for '
                    'files with a given file extension. Then it copies these '
                    'files from the source location to a destination folder')

    parser.add_argument('-e', '--extension', help='file extension',
                        required='True')

    parser.add_argument('-s', '--src', help='path to the analyzed folder',
                        type=helpers.get_dir_path, default='.')

    parser.add_argument('-d', '--dst', help='path to the output folder',
                        required='True', type=helpers.get_outdir_path)

    args = parser.parse_args(sys.argv[1:])
    return (args.extension,
            args.src,
            args.dst)


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
