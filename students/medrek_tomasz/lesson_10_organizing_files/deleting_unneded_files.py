#!/usr/bin/env python3


import os
import sys
import re


def print_usage():
    print("Usage: delete_unneeded_files.pyw <size_of_file> <path>"
          "\nExample: delete_unneeded_files.pyw 100MB /tmp/delete_my_files")


def main():
    argc = len(sys.argv)

    if argc != 3:
        print_usage()
        exit()

    size_given = sys.argv[1].lower()
    dir_path = os.path.abspath(sys.argv[2])

    if not size_given[:1].isdigit():
        print("Given size is invalid, try again")
        exit()

    if 'k' in size_given[-2:]:
        multiplier = 1000
        unit = "KB"
    elif 'm' in size_given[-2:]:
        multiplier = 1000000
        unit = "MB"
    elif 'g' in size_given[-2:]:
        multiplier = 1000000000
        unit = "GB"
    elif 't' in size_given[-2:]:
        multiplier = 1000000000000
        unit = "TB"
    else:
        multiplier = 1
        unit = "B"

    size = int(*re.findall(r'^\d+', size_given))
    size_in_bytes = size * multiplier

    matched_files = 0
    for directory, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.getsize(file_path) > size_in_bytes:
                print(file_path)
                matched_files += 1

    print("Found {} files in {} larger than {}{}".format(
        matched_files, dir_path, size, unit))


if __name__ == "__main__":
    main()
