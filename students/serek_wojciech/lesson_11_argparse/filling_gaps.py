#!/usr/bin/env python3
"""Filling gaps exercise"""

import os
import shutil
import re
import argparse

FILE_EXT = '.txt'


def main():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Path to files',
                        default='.\\test_tree_gaps')
    parser.add_argument('--prefix', help='Filename prefix',
                        default='spam')
    args = parser.parse_args()

    last_file_num = 0
    next_file_number = 0
    for file in os.listdir(args.path):
        if re.match(r'{}\d{{3}}{}'.format(args.prefix, FILE_EXT), file):
            regex = re.compile(r'\d+')
            current_file_number = int(regex.search(file).group(0))
            if current_file_number != next_file_number:
                shutil.move(os.path.join(args.path, file),
                            os.path.join(args.path, '{}{:03d}{}'.format(
                                args.prefix, next_file_number, FILE_EXT)))
                last_file_num = next_file_number
            else:
                last_file_num = current_file_number
            next_file_number = last_file_num + 1


if __name__ == '__main__':
    main()
