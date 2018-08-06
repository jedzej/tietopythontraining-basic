#! python 3
# selective_copy.py walks through a folder tree, searches for files with
# extension .jpg and copies them into a new folder.

import shutil
import os
import argparse
import sys


def selective_copy(data):
    for file in os.listdir(data[0]):
        if file.endswith('.jpg'):
            shutil.copy(os.sep.join([(data[0]), file]), data[1])


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input directory parsing')
    parser.add_argument('-s', '--source',
                        help='Source directory for selective copy',
                        default= './')
    parser.add_argument('-t', '--target',
                        help='Target directory for selective copy',
                        required= True)

    results = parser.parse_args(args)
    return [results.source,
            results.target]


if __name__ == '__main__':
    selective_copy(check_arg(sys.argv[1:]))
