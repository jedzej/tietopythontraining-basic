import re
import os
import fnmatch
import argparse
import sys


def main():
    pattern = re.compile(r'{}'.format(check_args(sys.argv[1:])))
    txt_file_list = []
    for file in os.listdir(os.curdir):
        if fnmatch.fnmatch(file, "*.txt"):
            txt_file_list.append(file)

    for file in txt_file_list:
        with open(file) as reader:
            for line in reader:
                if re.match(pattern, line):
                    print(line)


def check_args(args=None):
    parser = argparse.ArgumentParser(description='Regex search')
    parser.add_argument('-p', '--pattern',
                        help='Pattern to look for',
                        required=True)

    result = parser.parse_args(args)
    return result.pattern


if __name__ == '__main__':
    main()
