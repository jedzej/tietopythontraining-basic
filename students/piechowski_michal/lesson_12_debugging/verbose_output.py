#!/usr/bin/env python3

import argparse
import glob
import logging
import re
import sys

logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


def check_arg(args):
    parser = argparse.ArgumentParser(
        description='Script to search for regex in all .txt files')
    parser.add_argument('-r', '--regex',
                        help='Regex to be searched (for example .*)',
                        required=True)
    parser.add_argument('-l', '--log',
                        choices=['disabled', 'warning', 'info'],
                        help='Log verbosity',
                        default='info')

    results = parser.parse_args(args)

    if results.log == 'disabled':
        return results.regex, logging.CRITICAL
    elif results.log == 'warning':
        return results.regex, logging.WARNING
    else:
        return results.regex, logging.INFO


def main():
    regex, verbosity = check_arg(sys.argv[1:])
    logging.getLogger().setLevel(verbosity)

    logging.info("Searching for following regex in .txt files: " + regex)
    pattern = re.compile(regex)

    for path in glob.glob("*.txt"):
        file = open(path, "r")
        for line in file:
            if pattern.match(line):
                logging.warning("line:\n" + line + "from file: " + path
                         + " matches!\n")


if __name__ == "__main__":
    main()
