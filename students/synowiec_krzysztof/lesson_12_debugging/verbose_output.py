import re
import os
import fnmatch
import argparse
import sys
import logging
from argparse import RawTextHelpFormatter


def main():
    pattern_str, level = check_args(sys.argv[1:])
    log_configuration(level)
    logging.info('Choosen pattern {}'.format(pattern_str))
    pattern = re.compile(r'{}'.format(pattern_str))
    txt_file_list = []
    logging.info('Looking for all txt files in current dir')
    for file in os.listdir(os.curdir):
        if fnmatch.fnmatch(file, "*.txt"):
            txt_file_list.append(file)
    logging.info('List of files found {}'.format(txt_file_list))

    if len(txt_file_list) == 0:
        logging.warning('No .txt files found')

    for file in txt_file_list:
        with open(file) as reader:
            for line in reader:
                if re.match(pattern, line):
                    print(line)


def check_args(args=None):
    parser = argparse.ArgumentParser(description='Verbose output. '
                                     'Script prints lines from current dir'
                                     'txt files which match provided pattern',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-p', '--pattern',
                        help='Pattern to look for',
                        required=True)
    parser.add_argument('-v', '--verbose',
                        help='verbose output, log level:\n'
                        'info - all,\n'
                        'warning - errors,\n'
                        'disable - no', default='info')
    result = parser.parse_args(args)
    return result.pattern, result.verbose


def log_configuration(level):
    logging.basicConfig(format='%(asctime)s - %(levelname)s- %(message)s')
    log_level = get_log_level(level)
    logging.getLogger().setLevel(log_level)


def get_log_level(level):
    if level == 'disable':
        return logging.CRITICAL
    elif level == 'warning':
        return logging.WARNING
    elif level == 'info':
        return logging.INFO


if __name__ == '__main__':
    main()
