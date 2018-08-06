#!/usr/bin/env python3


import sys
import os
import re
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Script for searching "
                                     "pattern in txt files in given directory")
    parser.add_argument('-d', '--path',
                        help='path to directory',
                        required=True)
    parser.add_argument('-s', '--search',
                        help='regular expression search pattern',
                        required=True)

    results = parser.parse_args(args)

    return(results.path, results.regex)


def main():
    string_from_file = ""
    count_files = 0
    count_lines = 0

    dir_path, pattern = check_arg(sys.argv[1:])

    if not os.path.isdir(dir_path):
        print("Directory not found")
        exit()

    regex = re.compile(pattern)

    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            count_files += 1

            try:
                fh = open(os.path.join(dir_path, file), 'r')
                string_from_file = fh.readlines()
                fh.close()
            except (UnicodeDecodeError, PermissionError) as e:
                print(e)
                continue

            for number, line in enumerate(string_from_file):
                if regex.findall(line):
                    count_lines += 1
                    print("--- Regex: {}, file: {}, line: {}: ---".format(
                        pattern, file, number))
                    print(line)

    print("Statistics: \n"
          "Regex: {} found in {} lines across {} text files in {} directory.\n"
          .format(pattern, count_lines, count_files, dir_path))


if __name__ == "__main__":
    main()
