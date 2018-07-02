#!/usr/bin/env python3
"""Filling gaps exercise"""

import os
import shutil
import re

FILE_PREFIX = 'spam'
FILE_EXT = '.txt'
TEST_FOLDER = 'test_tree_gaps'


def main():
    """Main function"""
    last_file_num = 0
    for file in os.listdir(TEST_FOLDER):
        if re.match(r'{}\d{{3}}{}'.format(FILE_PREFIX, FILE_EXT), file):
            regex = re.compile(r'\d+')
            current_file_number = int(regex.search(file).group(0))
            next_file_number = last_file_num + 1
            if current_file_number != next_file_number:
                shutil.move(os.path.join(TEST_FOLDER, file),
                            os.path.join(TEST_FOLDER, '{}{:03d}{}'.format(
                                FILE_PREFIX, next_file_number, FILE_EXT)))
                last_file_num = next_file_number
            else:
                last_file_num = current_file_number


if __name__ == '__main__':
    main()
