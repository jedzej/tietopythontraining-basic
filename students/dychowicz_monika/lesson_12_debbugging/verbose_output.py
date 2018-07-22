import os
import re
import argparse
import logging

logging.basicConfig(format=' %(asctime)s - %(levelname)s- %(message)s')


def check_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex",
                        help="regex",
                        default=".*")
    parser.add_argument("-d", "--directory",
                        help="directory",
                        default=r"C:\Python36\files")
    parser.add_argument("-v", "--verbose",
                        help="verbose level",
                        choices=['disabled', 'warning', 'info'],
                        default="warning")
    results = parser.parse_args(args)
    return results.regex, results.directory, results.verbose


def set_verbose_level(verbose_level):
    logger = logging.getLogger()
    if verbose_level == "info":
        logger.setLevel(logging.INFO)
    elif verbose_level == "warning":
        logger.setLevel(logging.WARNING)
    else:
        logger.disabled = True


def regex_search(reg, folder):
    regex_text = re.compile(reg)
    logging.info("Regex = {}".format(regex_text))
    files_list = os.listdir(folder)
    logging.info("Files: {}".format(files_list))
    for file in files_list:
        if file.endswith('.txt'):
            logging.info("Textfile found: {}".format(file))
            with open(os.path.join(folder, file)) as textfile:
                for line in textfile:
                    if regex_text.match(line):
                        print("Regex found " + line)
                        logging.info("Regex found " + line)
                    else:
                        logging.warning("Regex not found" + line)
        else:
            logging.warning("File {} is not a text file".format(file))


if __name__ == '__main__':
    regex, directory, level = check_args()
    set_verbose_level(level)
    regex_search(regex, directory)