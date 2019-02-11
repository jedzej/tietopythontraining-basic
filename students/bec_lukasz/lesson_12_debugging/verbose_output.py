import os
import re
import argparse
import logging

# -f "c:\Pajton" -r "(\w+)(@)(\w+)(\.{1})(\w+)" -v "w"

# Verbose output - add configurable logger and 'verbose output'
# command line argument to project 1 from lesson 11 to allow the
# user to follow intermediate steps of program execution.
# The program must allow to configure verbosity on at least 3
# levels - disabled, warning (warns and errors only)
# and info (most detailed)


def set_logging():
    logging.basicConfig(level=logging.NOTSET)
    logging.basicConfig(level=logging.INFO,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.WARNING,
                        format='s - %(asctime)s - %(levelname)s - %(message)s')


def pick_arguments():

    parser = argparse.ArgumentParser(description='Searching for regex')
    parser.add_argument('-f', '--folder', action="store", type=str)
    parser.add_argument('-r', '--regex', action="store", type=str)
    parser.add_argument('-v', '--verbose', dest='verbose',
                        help='Logging level', choices=['n', 'i', 'w'],
                        default='n')
    arguments = parser.parse_args()

    target_folder_path = arguments.folder
    target_regex = re.compile(arguments.regex)
    logging_level = arguments.verbose

    return target_folder_path, target_regex, logging_level


def regex_debug(method):
    target_folder_path = pick_arguments()[0]
    target_regex = pick_arguments()[1]
    for file in os.listdir(target_folder_path):
        if '.txt' in file:
            txt_file = open(os.path.join(target_folder_path, file), 'r')
            content = txt_file.read()
            txt_file.close()
            result = target_regex.search(content)
            try:
                method(result.group())
            except AttributeError:
                method('Not found')


def check_logging_level(level):
    if level == 'n':
        regex_debug(print)
    elif level == 'i':
        regex_debug(logging.info)
    elif level == 'w':
        regex_debug(logging.warning)


def main():
    set_logging()
    check_logging_level(pick_arguments()[2])


if __name__ == '__main__':
    main()
