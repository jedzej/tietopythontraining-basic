"""
Verbose output - add configurable logger and 'verbose output'
command line argument to project 1 from lesson 11 to allow
the user to follow intermediate steps of program execution.
The program must allow to configure verbosity on at least 3
levels - disabled, warning (warns and errors only)
and info (most detailed)
"""

import argparse
import logging
import os
import re
import sys

LOG_LEVELS = {"debug": logging.DEBUG,
              "info": logging.INFO,
              "warning": logging.WARNING,
              "error": logging.ERROR,
              "critical": logging.CRITICAL}


def args_parameters(args):
    parser = argparse.ArgumentParser(
        description='Saerch for a specific pattern:')
    parser.add_argument('-d', '--directory',
                        help="directory to parse files", default=os.getcwd())
    parser.add_argument('-s', '--suffix',
                        help='File type(suffix)', default="")
    parser.add_argument('-r', '--regex',
                        help="Phrase to search", required=True)
    parser.add_argument('-l', '--logger',
                        help="Log level: debug, info, warning, error, critical",
                        default="debug",)
    result = parser.parse_args()

    return result.directory, result.suffix, result.regex, result.logger


directory, suffix, regex, log_level = args_parameters(sys.argv)
logging.basicConfig(level=LOG_LEVELS[log_level], format='%(asctime)s '
                    '- %(levelname)s - %(message)s')


def search(path, suf, reg):
    pattern = re.compile(reg)

    for folderName, subfolders, filenames in os.walk(path):
        for file in filenames:
            logging.debug("Checking file: " + file)
            if file.endswith(suf):
                input_file = open(os.path.join(folderName, file))
                lines = input_file.readlines()
                for line in lines:
                    if pattern.search(line):
                        logging.debug(file + ": " + line.rstrip())
                input_file.close()


def main():
    search(directory, suffix, regex)


if __name__ == '__main__':
    main()
