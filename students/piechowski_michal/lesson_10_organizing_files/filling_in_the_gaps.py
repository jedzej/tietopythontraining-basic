#!/usr/bin/env python3

import glob
import os
import re

dir_path = "test_tree2/"
prefix = "spam"
sufix = ".txt"
path_format = dir_path + prefix + "*" + sufix
enumerate_pattern = re.compile(r'.*(\d{3})' + sufix)

files_dictionary = {}


def fill_files_dictionary():
    for path in glob.glob(path_format, recursive=True):
        if enumerate_pattern.match(path):
            id = int(enumerate_pattern.match(path).group(1))
            files_dictionary[id] = path


def print_gaps(sorted_ids):
    max_id = sorted_ids[-1]
    for i in range(1, max_id):
        if i not in sorted_ids:
            print("Gap at: " + str(i).zfill(3))


def fill_gaps(sorted_ids):
    for i in range(0, len(sorted_ids)):
        path = files_dictionary[sorted_ids[i]]
        destination = dir_path + prefix + str(i + 1).zfill(3) + sufix
        os.rename(path, destination)


def main():
    fill_files_dictionary()
    sorted_ids = sorted(files_dictionary.keys())

    print_gaps(sorted_ids)
    fill_gaps(sorted_ids)


if __name__ == "__main__":
    main()
