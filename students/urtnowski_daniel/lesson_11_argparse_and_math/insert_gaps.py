#!/usr/bin/env python3

"""
insert_gaps.py: a practice project "Filling in the Gaps - extra challenge"
from: https://automatetheboringstuff.com/chapter9/

The program inserts gaps into numbered files so that a new file can be added

Usage: insert_gaps.py [-h] -p PREFIX -s START -l LEN [-d PATH]

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
        description='The program inserts gaps into numbered files so that '
                    'a new file can be added')

    parser.add_argument('-p', '--prefix', help='prefix used in file-names',
                        required='True')

    parser.add_argument('-s', '--start', help='first number to be shifted',
                        required='True', type=helpers.get_positive_int)

    parser.add_argument('-l', '--len', help='length of the gap in numbering',
                        required='True', type=helpers.get_positive_int)

    parser.add_argument('-d', '--path', help='path to the analyzed folder',
                        type=helpers.get_dir_path, default='.')

    args = parser.parse_args(sys.argv[1:])

    return (args.prefix,
            args.start,
            args.len,
            args.path)


def main():

    prefix, start, gap_len, path = get_args()
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

    if numbers[-1] != files_count:
        print('Error! There are already gaps in the files numbers')
        return

    if start > files_count:
        # nothing to do
        return

    for i in range(files_count - 1, start - 2, -1):
        old_name = '{}{:0{num_len}d}{}'.format(prefix, numbers[i], postfix,
                                               num_len=number_len)
        old_path = os.path.join(path, old_name)
        new_name = '{}{:0{num_len}d}{}'.format(prefix, i + 1 + gap_len,
                                               postfix, num_len=number_len)
        new_path = os.path.join(path, new_name)
        shutil.move(old_path, new_path)


if __name__ == '__main__':
    main()
