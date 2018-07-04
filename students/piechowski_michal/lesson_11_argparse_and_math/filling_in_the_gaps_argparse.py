#!/usr/bin/env python3

import argparse
import glob
import os
import re
import sys

files_dictionary = {}


def check_arg(args):
    parser = argparse.ArgumentParser(description='Script for filling the gaps')
    parser.add_argument('-i', '--input_dir',
                        help='Input directory where gaps should be filled',
                        default="test_tree2")
    parser.add_argument('-p', '--prefix',
                        help='File prefix (e.g. spam)',
                        required=True)
    parser.add_argument('-s', '--sufix',
                        help='File sufix (e.g. .txt)',
                        required=True)

    results = parser.parse_args(args)
    results.input_dir += "/"

    return results.input_dir, results.prefix, results.sufix


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
    global dir_path, prefix, sufix, path_format, enumerate_pattern

    dir_path, prefix, sufix = check_arg(sys.argv[1:])
    path_format = dir_path + prefix + "*" + sufix
    enumerate_pattern = re.compile(r'.*(\d{3})' + sufix)

    fill_files_dictionary()
    sorted_ids = sorted(files_dictionary.keys())

    print_gaps(sorted_ids)
    fill_gaps(sorted_ids)


if __name__ == "__main__":
    main()
