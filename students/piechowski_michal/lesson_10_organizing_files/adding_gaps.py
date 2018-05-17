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


def print_files(sorted_ids):
    for i in sorted_ids:
        print("File id: " + str(i))


def add_gap(sorted_ids):
    gap = int(input("\nChoose on of above ids to add gap: "))
    if gap not in sorted_ids:
        print("Such id doesn't exist")
        exit()

    for i in reversed(sorted_ids):
        path = files_dictionary[i]
        destination = dir_path + prefix + str(i + 1).zfill(3) + sufix
        os.rename(path, destination)
        if i == gap:
            break


def main():
    fill_files_dictionary()
    sorted_ids = sorted(files_dictionary.keys())

    print_files(sorted_ids)
    add_gap(sorted_ids)


if __name__ == "__main__":
    main()
