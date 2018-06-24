"""
Write a program that opens all .txt files in a folder and
searches for any line that matches a user-supplied regular
expression. The results should be printed to the screen.
"""

import argparse
import os
import re
import sys


def args_parameters(args):
    parser = argparse.ArgumentParser(
        description='Saerch for a specific pattern:')
    parser.add_argument('-d', '--directory',
                        help="directory to parse files", default=os.getcwd())
    parser.add_argument('-s', '--suffix', help='File type(suffix)', default="")
    parser.add_argument('-r', '--regex', help="Phrase to search", required=True)

    result = parser.parse_args()

    return result.directory, result.suffix, result.regex


directory, suffix, regex = args_parameters(sys.argv)


def search(path, suf, reg):
    pattern = re.compile(reg)

    for folderName, subfolders, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(suf):
                input_file = open(os.path.join(folderName, file))
                lines = input_file.readlines()
                for line in lines:
                    if pattern.search(line):
                        print(file + ": " + line.rstrip())
                input_file.close()


def main():
    search(directory, suffix, regex)


if __name__ == '__main__':
    main()
