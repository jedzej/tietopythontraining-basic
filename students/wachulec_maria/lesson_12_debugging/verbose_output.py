import os
import re
import argparse
import sys
import logging


def logger_lever_chooser(level):
    if level == 'd':
        logging.basicConfig(level=logging.CRITICAL,
                            format=' %(asctime)s - %(levelname)s- %(message)s')
    elif level == 'w':
        logging.basicConfig(level=logging.WARNING,
                            format=' %(asctime)s - %(levelname)s- %(message)s')
    elif level == 'i':
        logging.basicConfig(level=logging.INFO,
                            format=' %(asctime)s - %(levelname)s- %(message)s')


def check_arg(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', '--regex', dest='regex',
                        help='Regular expression to search in txt files',
                        default=r"\w\d")
    parser.add_argument('-v', '--verbose', dest='verbose',
                        help='Logging level', choices=['d', 'w', 'i'],
                        default='i')
    results = parser.parse_args(args)
    return results.regex, results.verbose


def search_in_file(file, reg):
    txt_file = open(os.path.join(os.getcwd(), file))
    text = txt_file.read()
    regex = re.findall(reg, text)
    if not regex:
        logging.warning('There are no matching text in this file')
    txt_file.close()
    return regex


def print_result(result):
    return '\n'.join([str(i) + ': ' + str(result[i]) for i in result.keys()
                      if result[i] != []])


def search_regex():
    regular_expression, log_level = check_arg(sys.argv[1:])
    logger_lever_chooser(log_level)
    logging.info('Start of program')
    logging.info('Regex was downloaded from parser. Regex: {}'.
                 format(regular_expression))
    regex_in_file = {}
    file_list = os.listdir(os.getcwd())
    amount_file = 0
    for file in file_list:
        if file.endswith('.txt'):
            amount_file += 1
            logging.info('Checking in the {} file'.format(file))
            regex_in_file[file] = search_in_file(file, regular_expression)
    if len(regex_in_file.values()) == amount_file:
        logging.error('There are no matching text in ALL files')
    logging.info('End of program')
    return print_result(regex_in_file)


print(search_regex())
