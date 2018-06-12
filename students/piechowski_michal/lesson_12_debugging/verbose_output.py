#!/usr/bin/env python3

import argparse
import glob
import re
import sys


verbosity = ""


def my_print(tag, text):
    if verbosity == "disabled":
        return
    if tag == "warning" or verbosity == "info":
        print(text)


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
    return results.regex, results.log


def main():
    global verbosity
    regex, verbosity = check_arg(sys.argv[1:])
    my_print("info", "Searching for following regex in .txt files: " + regex)
    pattern = re.compile(regex)

    for path in glob.glob("*.txt"):
        file = open(path, "r")
        for line in file:
            if pattern.match(line):
                my_print("warning", "line:\n" + line + "from file: " + path
                         + " matches!\n")


if __name__ == "__main__":
    main()
