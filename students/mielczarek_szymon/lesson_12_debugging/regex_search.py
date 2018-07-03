#! python3
import os
import re
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def set_verbosity_level(verbose_lvl):
    if verbose_lvl == 0:
        logging.disable(logging.CRITICAL)
    elif verbose_lvl == 1:
        logger.setLevel(logging.WARNING)
    elif verbose_lvl == 2:
        logger.setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser(description='Regex Search program with '
                                                 'verbose output.')
    parser.add_argument('-r', '--regex', help="Regex to match", required=True)
    parser.add_argument('-v', '--verbosity',
                        help="Verbosity level. 0 - disabled, "
                             "1 - warnings and errors, "
                             "2 - info. Verbose output is disabled by default.",
                        type=int, default=0)
    args = parser.parse_args()

    set_verbosity_level(args.verbosity)

    count = 0
    regex = re.compile(r'{}'.format(args.regex))
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                logger.info("File opened: %s", filename)
                count += 1
                for line in file.readlines():
                    if regex.match(line):
                        print(line)

    if count == 0:
        logger.warning("No .txt files found in the current directory.")


if __name__ == "__main__":
    main()
