#!/usr/bin/env python3

import argparse
import glob
import re
import sys


def check_arg(args):
    parser = argparse.ArgumentParser(description='Script to search for regex in all .txt files')
    parser.add_argument('-r', '--regex',
                        help='Regex to be searched (for example .*)',
                        required=True)

    results = parser.parse_args(args)
    return results.regex


def main():
    regex = check_arg(sys.argv[1:])
    print("Searching for following regex in all .txt files: " + regex)
    pattern = re.compile(regex)

    for path in glob.glob("*.txt"):
        file = open(path, "r")
        for line in file:
            if pattern.match(line):
                print("line:\n" + line + "from file: " + path + " matches!\n")


if __name__ == "__main__":
    main()
