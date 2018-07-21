import os
import argparse
import logging
import re


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
                        dest='choice',
                        default='info')

    args = parser.parse_args()

    if args.choice == 'disabled':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.choice == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)

    regex = re.compile(r'{}'.format(args.regex))
    logging.info("Searching for regex: " + args.regex + " within .txt files")

    found = False
    for file_name in os.listdir('.'):
        if file_name.endswith(".txt"):
            with open(file_name) as file:
                for line in file.readlines():
                    if regex.match(line):
                        found = True
                        logging.info(line)

    if not found:
        logging.warning("Searching for regex: " + args.regex + " failed!")


if __name__ == "__main__":
    main()
