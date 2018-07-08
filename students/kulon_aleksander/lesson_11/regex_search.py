#! python3
import os
import re
import argparse
import sys

"""
The program opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression.
The results are then printed to the screen.
"""


def main():
    parser = argparse.ArgumentParser(
        description='Searching for regex within .txt files')
    parser.add_argument('-r', '--regex',
                        help='Regex to be searched',
                        required=True)

    args = parser.parse_args()
    regex = re.compile(r'{}'.format(args.regex))
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                for line in file.readlines():
                    if regex.match(line):
                        print(line)


if __name__ == "__main__":
    main()
