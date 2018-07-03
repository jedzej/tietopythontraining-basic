"""
Write a program that opens all .txt files in a folder and
searches for any line that matches a user-supplied regular
expression. The results should be printed to the screen.
"""

import os
import re


def main():
    files = os.listdir()
    print("Please input a pattern to search:")
    regex = str(input())
    for file in files:
        input_file = open(file)
        lines = input_file.readlines()
        for line in lines:
            pattern = re.compile(regex)
            if pattern.search(line):
                print(file + ": " + line.rstrip())
        input_file.close()


if __name__ == '__main__':
    main()
