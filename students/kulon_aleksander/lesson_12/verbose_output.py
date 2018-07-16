#! python3
import os
import re
import argparse
import logging

logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')

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
    parser.add_argument('-v', '--verbose',
                        help='log level',
                        choices=['disabled', 'warning', 'info'],
                        default='info')

    args = parser.parse_args()

    if args.verbose == 'disabled':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.verbose == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)

    regex = re.compile(r'{}'.format(args.regex))
    logging.info("Searching for regex: " + args.regex + " within .txt files")

    found = False
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                for line in file.readlines():
                    if regex.match(line):
                        found = True
                        logging.info(line)

    if not found:
        logging.warning("Searching for regex: " + args.regex + " failed!")


if __name__ == "__main__":
    main()
