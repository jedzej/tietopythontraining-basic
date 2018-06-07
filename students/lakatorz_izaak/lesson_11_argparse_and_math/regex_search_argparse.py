import os
import re
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Regex search.')

    user_regex = re.compile(r'\d')

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default='../lesson_11_argparse_and_math/')
    parser.add_argument(
        '-e', action="store",
        dest='extension',
        required='True'
    )
    results = parser.parse_args(sys.argv[1:])

    folder_files = os.listdir(results.path)

    txt_files = [x for x in folder_files if x.endswith(results.extension)]

    for filename in txt_files:
        file = open(results.path + filename)
        for line in file.readlines():
            checked_line = user_regex.search(line)
            if checked_line is not None:
                print(filename + ' : ' + line)


if __name__ == '__main__':
    main()
