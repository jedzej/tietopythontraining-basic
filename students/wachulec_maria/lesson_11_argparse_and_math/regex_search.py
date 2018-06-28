import os
import re
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', '--regex', dest='regex',
                        help='Regular expression to search in txt files',
                        default=r"\w\d")
    results = parser.parse_args(args)
    return results.regex


def search_in_file(file, reg):
    txt_file = open(os.path.join(os.getcwd(), file))
    text = txt_file.read()
    regex = re.findall(reg, text)
    txt_file.close()
    return regex


def print_result(result):
    return '\n'.join([str(i) + ': ' + str(result[i]) for i in result.keys()
                      if result[i] != []])


def search_regex():
    regular_expression = check_arg(sys.argv[1:])
    regex_in_file = {}
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            regex_in_file[file] = search_in_file(file, regular_expression)
    return print_result(regex_in_file)


print(search_regex())
