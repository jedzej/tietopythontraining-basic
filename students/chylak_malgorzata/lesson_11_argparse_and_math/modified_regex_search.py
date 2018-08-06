import re
import os
import sys
import argparse


def regex_search(spritna_nazwa):
    regex = re.compile(r'{}'.format(spritna_nazwa))
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                for line in file.readlines():
                    found = regex.findall(line)
                    if found:
                        print(found)
                    if regex.match(line):
                        print(regex.findall(line))
                        print(line)


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input a search parameter')
    parser.add_argument('-s', '--search',
                        help='Regular Expression',
                        required=True)

    results = parser.parse_args(args)
    return results.search


if __name__ == '__main__':
    regex_search(check_arg(sys.argv[1:]))
