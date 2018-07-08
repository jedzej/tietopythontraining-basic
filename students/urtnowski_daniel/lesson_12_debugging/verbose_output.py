#!/usr/bin/env python3

"""
verbose_output.py: a practice project: "Verbose output" from:
Lesson 12 - Debugging

The program is based on regex_search.py with configurable logger added.

Usage: verbose_output.py [-h] -r REGEX [-p PATH] [-V {0,1,2}]
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import re
import os
import sys
import argparse
import enum
import datetime


class Logger:
    def __init__(self, log_level):
        self.level = log_level

    def set_level(self, log_level):
        self.level = log_level

    def info(self, message):
        if self.level == Logger.LogLevel.INFO:
            print('[{}] INFO: {}'.format(Logger._get_timestamp(), message))

    def warning(self, message):
        if self.level != Logger.LogLevel.DISABLED:
            print('[{}] WARNING: {}'.format(Logger._get_timestamp(), message))

    @staticmethod
    def _get_timestamp():
        now = datetime.datetime.now()
        timestamp = '{:%H:%M %d.%m.%Y}'.format(now)
        return timestamp

    class LogLevel(enum.Enum):
        DISABLED = 0
        INFO = 1
        WARNING = 2


def get_dir_path(path):
    """
    This function verifies if the input string is a valid directory path
    :param string path: The path to be verified
    :return string: The absolute path to the directory passed as input
    :raises: argparse.ArgumentTypeError when the path is invalid
    """
    if not os.path.exists(path) or not os.path.isdir(path):
        raise argparse.ArgumentTypeError('"{}" is not a valid directory!'
                                         .format(path))
    if not os.path.isabs(path):
        path = os.path.abspath(path)

    return path


def get_args():
    parser = argparse.ArgumentParser(
        description='The program opens all *.txt files in a given folder and '
                    'searches for any line that matches a user-supplied '
                    'regular expression')

    parser.add_argument('-r', '--regex', help='regex string', required='True')

    parser.add_argument('-p', '--path', help='path to the analyzed folder',
                        type=get_dir_path, default='.')

    parser.add_argument('-V', '--verbose-output', dest='log_level',
                        help='logging level: 0 - disable, 1 - info, 2 - '
                             'warning. By default the logging is disabled',
                        type=int, choices=(0, 1, 2), default=0)

    args = parser.parse_args(sys.argv[1:])
    return (args.regex,
            args.path,
            Logger.LogLevel(args.log_level))


def main():

    pattern, dir_path, log_level = get_args()
    logger = Logger(log_level)

    logger.info('Program start; regex pattern = {}, source dir path = {}'
                .format(re.escape(pattern), dir_path))

    try:
        os.chdir(dir_path)
        regex = re.compile(pattern)

        for filename in os.listdir(dir_path):
            logger.info('Checking folder: {}'.format(dir_path))

            if filename.endswith('.txt'):
                logger.info('Checking file: {}'.format(filename))
                file = open(filename, 'r')
                for idx, line in enumerate(file):
                    mo = regex.search(line)

                    if mo is not None:
                        print('[{}:{}] {}'.format(filename, idx + 1, line),
                              end='')
                file.close()
            else:
                logger.info('Omitting file: {}'.format(filename))

    except Exception as ex:
        logger.warning('Critical error: {}'.format(ex))

    logger.info('Program end')


if __name__ == '__main__':
    main()
