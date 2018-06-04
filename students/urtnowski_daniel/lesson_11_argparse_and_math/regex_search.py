#!/usr/bin/env python3

"""
regex_search.py: a practice project: "Regex Search" from:
https://automatetheboringstuff.com/chapter8/

The program opens all *.txt files in a given folder and searches for any line
that matches a user-supplied regular expression.

Usage: regex_search.py [-h] -r REGEX [-p PATH]
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import re
import os
import sys
import argparse
import helpers


def get_args():
    parser = argparse.ArgumentParser(
        description='The program opens all *.txt files in a given folder and '
                    'searches for any line that matches a user-supplied '
                    'regular expression')

    parser.add_argument('-r', '--regex', help='regex string', required='True')

    parser.add_argument('-p', '--path', help='path to the analyzed folder',
                        type=helpers.get_dir_path, default='.')

    args = parser.parse_args(sys.argv[1:])
    return args.regex, args.path


def main():

        pattern, dir_path = get_args()

        os.chdir(dir_path)
        regex = re.compile(pattern)

        for filename in os.listdir(dir_path):
            if filename.endswith('.txt'):
                file = open(filename, 'r')
                for idx, line in enumerate(file):
                    mo = regex.search(line)

                    if mo is not None:
                        print('[{}:{}] {}'.format(filename, idx + 1, line),
                              end='')
                file.close()


if __name__ == '__main__':
    main()
