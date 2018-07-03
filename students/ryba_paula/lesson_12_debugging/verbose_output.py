import re
import os
import argparse
import sys
import logging

logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')


def arg_input(args):
    parser = argparse.ArgumentParser(description="This script searches for "
                                                 "given regex in .txt files")
    parser.add_argument('-r', '--regex', help='regex to be checked',
                        required=True)
    parser.add_argument('-v', '--verbose',
                        help='log level',
                        choices=['disabled', 'warning', 'info'], required=True)
    results = parser.parse_args(args)
    return results.regex, results.verbose


reg, log_level = arg_input(sys.argv[1:])


def set_log_level(lvl):
    logger = logging.getLogger()
    if lvl == 'disabled':
        return logging.disable(logging.CRITICAL)
    elif lvl == 'warning':
        return logger.setLevel(logging.WARNING)
    elif lvl == 'info':
        return logger.setLevel(logging.INFO)


def regex_search():
    set_log_level(log_level)

    regex = re.compile(reg)
    logging.info("Regex is {}".format(regex))

    files_list = os.listdir('.')
    logging.info("Files: {}".format(files_list))

    for el in files_list:
        if el.endswith('.txt'):
            logging.info(".txt file found")
            with open(el) as infile:
                for line in infile:
                    if regex.match(line):
                        print("Matched! " + line)
                        logging.info("match found")
                    else:
                        logging.warning("match not found")
        else:
            logging.warning("{} is not a .txt file".format(el))


if __name__ == '__main__':
    regex_search()
