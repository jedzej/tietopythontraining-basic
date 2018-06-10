import re
import os
import argparse
import sys


def arg_input(args):
    parser = argparse.ArgumentParser(description="Regex search")
    parser.add_argument('-r', '--regex', help="Regex to be checked",
                        required=True)
    results = parser.parse_args(args)
    return results.regex


def regex_search():
    reg = arg_input(sys.argv[1:])
    regex = re.compile(reg)
    files_list = os.listdir('.')

    for el in files_list:
        if el.endswith(".txt"):
            with open(el) as infile:
                for line in infile:
                    if regex.match(line):
                        print("Matched! " + line)


if __name__ == '__main__':
    regex_search()
