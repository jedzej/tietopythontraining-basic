#!/usr/bin/env python3


import os
import sys
import shutil
import errno


def print_usage():
    print("Usage: selective_copy.pyw <file_extension> <source> <destination>"
          "\nExample: selective_copy.pyw pdf ~/Downloads/ ~/Documents/")


def main():
    argc = len(sys.argv)

    if argc != 4:
        print_usage()
        exit()

    file_extension = sys.argv[1]
    source = os.path.abspath(sys.argv[2])
    destination = os.path.abspath(sys.argv[3])

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
