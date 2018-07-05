#! python3
import os
import re

"""
The program opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression.
The results are then printed to the screen.
"""


def main():
    regex = re.compile(r'{}'.format(input("Enter regular expression: ")))
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                for line in file.readlines():
                    if regex.match(line):
                        print(line)


if __name__ == "__main__":
    main()
