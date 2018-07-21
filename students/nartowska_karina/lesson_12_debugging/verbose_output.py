import re
import glob
import argparse
import sys
import logging


LOGGER_LEVELS = {"debug": logging.DEBUG,
                 "info": logging.INFO,
                 "warning": logging.WARNING,
                 "error": logging.ERROR}


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Regex search')
    parser.add_argument('-r', '--regex',
                        help='search regex',
                        required=True)

    parser.add_argument('-v', '--verbose',
                        help='verbose output: debug, info, warning, error',
                        default='debug')

    results = parser.parse_args(args)
    return (results.regex,
            results.verbose)


regex, verbose = check_arg(sys.argv)
logging.basicConfig(level=LOGGER_LEVELS[verbose],
                    format='%(asctime)s - %(levelname)s - %(message)s')


def search_regex(regex_search):
    for file in glob.glob("*.txt"):
        current = open(file)
        logging.debug("File: " + file)
        content = current.readlines()
        for line in content:
            if regex_search.match(line):
                logging.debug("Correct line is:\n" + line + "from file: " + file)

        current.close()


def main():
    reg = check_arg(sys.argv[1:])
    logging.debug("Searching regex in .txt files: " + reg)
    regex_search = re.compile(reg)
    search_regex(regex_search)


if __name__ == "__main__":
    main()
