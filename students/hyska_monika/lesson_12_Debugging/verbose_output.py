"""
Program that opens all .txt files in a folder and
searches for any line that matches a user-supplied regular expression.
The results should be printed to the screen.
"""

import re
import os
import argparse
import sys
import logging
import logging_set


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Search regex on files')
    parser.add_argument('-p', '--path',
                        help='path to search',
                        default='./')
    parser.add_argument('-r', '--regex',
                        required='True',
                        help='regex to search')
    parser.add_argument('-l', '--logs',
                        help='set log level')
    results = parser.parse_args(args)
    return (results.path,
            results.regex,
            results.logs)


def files_in_path(path):
    # check directory exists
    try:
        only_files = [f for f in os.listdir(path)
                      if os.path.isfile(os.path.join(path, f))]
        return only_files
    except OSError as err:
        if isinstance(err, FileNotFoundError):
            logging.error(err)
            sys.exit(1)


def search_regex(path, regex, logs):
    if logs not in(logging._nameToLevel):
        raise ValueError('Invalid log level: %s' % logs)
    directory = "./logs"
    logging_set.create_logsfile('verbose_logs.log', directory, logs)
    if path == directory:
        logging.warning('You should not search data in logs. Program closed.')
        sys.exit(1)
    files = files_in_path(path)
    pattern = re.compile(regex)
    print("Lines contain searched regex:")
    for file_name in files:
        file_with_path = os.path.join(path, file_name)
        logging.info('Checked file %s' % file_with_path)
        file_text = open(file_with_path)
        for line in file_text:
            line = line.rstrip()
            if re.search(pattern, line):
                print(str(file_name) + ": " + str(line))
                logging.info('Founded: %s in %s (%s file)' % (regex, line, file_name))
        file_text.close()
    logging.info('End searching')
    print("")


def main():
    my_path, my_regex, logs = check_arg(sys.argv[1:])
    search_regex(my_path, my_regex, logs)
    """
    my_path = "./txt_files"
    my_regex = "Ala\d{4}"
    search_regex(my_path, my_regex)
    my_regex = "^@"
    search_regex(my_path, my_regex)
    """


if __name__ == '__main__':
    main()
