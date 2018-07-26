#!/usr/bin/env python3


import sys
import os
import re
import argparse
import logging


DEFAULT_DEBUG_LVL = 1


logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Script for searching "
                                     "pattern in txt files in given directory")
    parser.add_argument('-d', '--path',
                        help='path to directory',
                        required=True)
    parser.add_argument('-s', '--search',
                        help='regular expression search pattern',
                        required=True)
    parser.add_argument('-v', '--verbosity',
                        help="debug level:\n0 - disabled,\n"
                        "1 - errors/warnings [default],\n"
                        "2 - all",
                        type=int,
                        default=DEFAULT_DEBUG_LVL,
                        required=False)

    results = parser.parse_args(args)

    return(results.path, results.search, results.verbosity)


def set_debug_level(dbg_lvl):
    if dbg_lvl not in [0, 1, 2]:
        logger.error("Incorrect verbosity lvl, using default one")
        dbg_lvl = DEFAULT_DEBUG_LVL

    if dbg_lvl == 2:
        logger.setLevel(logging.DEBUG)
    elif dbg_lvl == 1:
        logger.setLevel(logging.WARNING)
    else:
        logging.disable(logging.CRITICAL)


def main():
    string_from_file = ""
    count_files = 0
    count_lines = 0

    dir_path, pattern, verbosity = check_arg(sys.argv[1:])

    set_debug_level(verbosity)

    if not os.path.isdir(dir_path):
        logger.critical("Directory not found")
        exit()

    regex = re.compile(pattern)

    for file in os.listdir(dir_path):
        if file.endswith(".txt"):
            count_files += 1

            try:
                fh = open(os.path.join(dir_path, file), 'r')
                string_from_file = fh.readlines()
                fh.close()
            except (UnicodeDecodeError, PermissionError) as e:
                logger.error(e)
                continue

            for number, line in enumerate(string_from_file):
                if regex.findall(line):
                    count_lines += 1
                    logger.debug("Regex: {}, file: {}, line: {}".format(
                        pattern, file, number))
                    logger.debug(line)

    print("Statistics: \n"
          "Regex: {} found in {} lines across {} text files in {} directory.\n"
          .format(pattern, count_lines, count_files, dir_path))


if __name__ == "__main__":
    main()
