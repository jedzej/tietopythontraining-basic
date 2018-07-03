#!/usr/bin/env python3

"""
insert_gaps.py: a practice project "Filling in the Gaps - extra challenge"
from: https://automatetheboringstuff.com/chapter9/

The program inserts gaps into numbered files so that a new file can be added

Usage: ./insert_gaps.py <prefix> <start_num> <gap_len> <folder_path>

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import sys
import os
import re
import shutil


def get_args():

    args_cnt = len(sys.argv)

    if args_cnt != 5:
        print('Usage: ./insert_gaps.py <prefix> <start_num> <gap_len>'
              ' <folder_path>')
        return None

    else:
        prefix, start, gap_len, path = sys.argv[1:]

        if not prefix:
            print('Error! Incorrect prefix!')
            return None

        if not start.isdigit() or not gap_len.isdigit():
            print('Error! Start position and gap length must be numbers')
            return None

        start = int(start)
        gap_len = int(gap_len)
        if not (start > 0 and gap_len > 0):
            print('Error! Start position and gap length must be positive '
                  'numbers')
            return None

        if not os.path.exists(path) or not os.path.isdir(path):
            print('Error! The path: {} is incorrect!'.format(path))
            return None

        if not os.path.isabs(path):
            path = os.path.abspath(path)

        return prefix, start, gap_len, path


def main():

    args = get_args()
    if args is not None:
        prefix, start, gap_len, path = args
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
