import argparse
import os
import sys
import re


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to find sentence'
                                                 ' in txt files ')
    parser.add_argument('-s', '--sentence',
                        help='sentence to find in txt files',
                        required=True)
    results = parser.parse_args(args)
    return results.sentence


def find_word_in_all_files(sentence):
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            with open(file) as reader:
                line_index = 0
                for line in reader:
                    line_index += 1
                    if re.search(r'{}'.format(sentence), line):
                        print('file : {}'.format(file))
                        print('line {}: {}'.format(line_index, line))
                    else:
                        print('Cannot find more sentences in files')


def main():
    find_word_in_all_files(check_arg(sys.argv[1:]))


if __name__ == '__main__':
    main()
