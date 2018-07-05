#!/usr/bin/env python3

"""
regex_search.py: a practice project: "Regex Search" from:
https://automatetheboringstuff.com/chapter8/

The program opens all *.txt files in a given folder and searches for any line
that matches a user-supplied regular expression.

Usage: ./regex_search.py <path> <regex_string>
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import re
import os
import sys


def main():
    args_cnt = len(sys.argv)

    if args_cnt != 3:
        print("Error! Incorrect parameters\n"
              "Usage: ./regex_search.py <path> <regex_string>")
    else:
        dir_path = sys.argv[1]
        pattern = sys.argv[2]

        if os.path.exists(dir_path):
            if not os.path.isabs(dir_path):
                dir_path = os.path.abspath(dir_path)

            if not os.path.isdir(dir_path):
                print('Error! The given path is not a folder!')

            else:
                os.chdir(dir_path)
                regex = re.compile(pattern)

                for filename in os.listdir(dir_path):
                    if filename.endswith('.txt'):
                        file = open(filename, 'r')
                        for idx, line in enumerate(file):
                            mo = regex.search(line)

                            if mo is not None:
                                print('[{}:{}] {}'.format(filename, idx + 1,
                                                          line), end='')
                        file.close()
        else:
            print('Error! Incorrect path given!')


if __name__ == '__main__':
    main()
