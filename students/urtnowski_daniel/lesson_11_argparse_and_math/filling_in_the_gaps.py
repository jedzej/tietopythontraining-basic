#!/usr/bin/env python3

"""
filling_in_the_gaps.py: a practice project "Filling in the Gaps" from:
https://automatetheboringstuff.com/chapter9/

The program finds in a single folder all files named with a given prefix
followed by a number and corrects any gaps in the numbering

Usage: filling_in_the_gaps.py [-h] -p PREFIX [-d PATH]

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os
import re
import shutil
import argparse
import helpers


def get_args():
    parser = argparse.ArgumentParser(
        description='The program finds in a single folder all files named with'
                    ' a given prefix followed by a number and corrects any '
                    'gaps in the numbering')

    parser.add_argument('-p', '--prefix', help='prefix used in file-names',
                        required='True')

    parser.add_argument('-d', '--path', help='path to the analyzed folder',
                        type=helpers.get_dir_path, default='.')

    args = parser.parse_args(sys.argv[1:])
    return args.prefix, args.path


def main():

    prefix, path = get_args()
    numbers = []
    postfix = ''
    number_len = 0

    pattern = "^({})(\d+)(.*$)".format(re.escape(prefix))
    regex = re.compile(pattern)

    for file in os.listdir(path):
        mo = regex.search(file)
        if mo is not None:
            number = mo.group(2)
            if not postfix:
                postfix = mo.group(3)
                number_len = len(number)
            numbers.append(int(number))

    if not numbers:    # There are no files matching the pattern given
        return

    numbers.sort()
    files_count = len(numbers)

    if numbers[-1] == files_count:  # There are no gaps in the numbering
        return

    first_gap_position = 1
    for i in range(files_count):
        if numbers[i] != i + 1:
            first_gap_position = i
            break

    for i in range(first_gap_position, files_count):
        old_name = '{}{:0{num_len}d}{}'.format(prefix, numbers[i], postfix,
                                               num_len=number_len)
        old_path = os.path.join(path, old_name)
        new_name = '{}{:0{num_len}d}{}'.format(prefix, i + 1, postfix,
                                               num_len=number_len)
        new_path = os.path.join(path, new_name)
        shutil.move(old_path, new_path)


if __name__ == '__main__':
    main()
