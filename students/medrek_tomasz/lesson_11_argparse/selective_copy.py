#!/usr/bin/env python3


import os
import sys
import shutil
import errno
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Script for copying "
                                     "files with given extension between dirs")
    parser.add_argument('-s', '--source',
                        help='path to source directory',
                        required=True)
    parser.add_argument('-d', '--destination',
                        help='path to destination directory',
                        required=True)
    parser.add_argument('-e', '--extension',
                        help='extension of files to copy',
                        required=True)

    results = parser.parse_args(args)

    return(results.source, results.destination, results.extension)


def main():

    source, destination, file_extension = check_arg(sys.argv[1:])

    try:
        os.makedirs(destination)
    except PermissionError as e:
        print(e)
        exit()
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    copied_files = 0
    for directory, _, files in os.walk(source):
        for file in files:
            if file.endswith(file_extension):
                try:
                    print(shutil.copy(os.path.join(directory, file),
                                      destination))
                except PermissionError as perm_err:
                    print(perm_err)
                    break
                copied_files += 1

    print("Copied {} files from {} into {}".format(
        copied_files, source, destination))


if __name__ == "__main__":
    main()
