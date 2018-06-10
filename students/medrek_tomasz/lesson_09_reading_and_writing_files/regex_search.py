#!/usr/bin/env python3


import sys
import os
import re


def print_usage():
    print("Usage: regex_search.py <path to directory>"
          ", you can enter path with prompt as well")


def main():
    string_from_file = ""
    count_files = 0
    count_lines = 0
    argc = len(sys.argv)

    if argc > 1:
        dir_path = sys.argv[1]
    else:
        print_usage()
        dir_path = input('Please enter valid path to directory:\n')

    if not os.path.isdir(dir_path):
        print("Directory not found")
        exit()

    pattern = input("Please enter desired regex pattern\n")
    regex = re.compile(pattern)

    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            count_files += 1

            fh = open(os.path.join(dir_path, file), 'r')
            string_from_file = fh.readlines()
            fh.close()

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
