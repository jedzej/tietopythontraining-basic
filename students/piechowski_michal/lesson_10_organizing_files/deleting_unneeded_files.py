#!/usr/bin/env python3

import glob
import os


def main():
    parent_dir = os.path.expanduser("~/Zips/")
    big_file_size = 100 * 1024 * 1024

    for path in glob.glob(parent_dir + "**/*", recursive=True):
        file_size = os.path.getsize(path)
        if file_size >= big_file_size:
            print(path + " has " + str(file_size) + " bytes")


if __name__ == "__main__":
    main()
