# !python 3
# filling_in_the_gaps finds all files with a given prefix, locates any gaps
# in numbering and renames files.

import os
import re
import argparse
import sys


def gaps(data):
    files_tab = []
    regex = re.compile(r'^' + data[1] + '\d{3}' + data[2] + '$')

    for _, _, files in os.walk(data[0]):
        for file in files:
            mo = re.search(regex, file)
            if mo is not None:
                files_tab.append(file)

    files_tab = sorted(files_tab)
    number_of_files = len(files_tab)

    new_names = []
    for i in range(1, number_of_files + 1):
        new_names.append(data[1] + "{:03d}".format(i) + data[2])

    for i in range(len(files_tab)):
        if new_names[i] != files_tab[i]:
            os.replace(data[0] + '\\' + files_tab[i],
                       data[0] + '\\' + new_names[i])


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input prefix parsing')
    parser.add_argument('-s', '--source',
                        help='Source directory',
                        default=sys.path[0])
    parser.add_argument('-p', '--prefix',
                        help='File prefix',
                        required=True)
    parser.add_argument('-f', '--suffix',
                        help='File suffix',
                        required=True)

    results = parser.parse_args(args)
    return [results.source,
            results.prefix,
            results.suffix]


if __name__ == '__main__':
    gaps(check_arg(sys.argv[1:]))
