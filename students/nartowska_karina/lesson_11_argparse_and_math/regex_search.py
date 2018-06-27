import re
import glob
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Regex search')
    parser.add_argument('-r', '--regex',
                        help='search regex',
                        required='True',
                        default='')
    return parser.parse_args(args).regex


def search_regex(regex_search):
    for file in glob.glob("*.txt"):
        current = open(file)
        content = current.readlines()
        for line in content:
            if regex_search.match(line):
                print("Correct line is:\n" + line + "from file: " + file)

        current.close()


def main():
    reg = check_arg(sys.argv[1:])
    print("Searching regex in .txt files: " + reg)
    regex_search = re.compile(reg)
    search_regex(regex_search)


if __name__ == "__main__":
    main()
