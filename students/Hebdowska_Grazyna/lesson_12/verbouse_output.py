import re
import glob
import argparse
import sys
import logging


LOGGING = {"debug": logging.DEBUG,
           "warning": logging.WARNING,
           "info": logging.INFO}


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Give searched regex: ')
    parser.add_argument('-q', '--question',
                        help='"Give searched regex: "',
                        default='\d\d\d')
    parser.add_argument('-l', '--logger',
                        help='Give logger level: disabled, warning or info',
                        default='debug')

    results = parser.parse_args(args)
    return (results.question, results.logger)


def search_for_regex(searched_regex):
    logging.info("Start")
    for evry_file in glob.glob("*.txt"):
        logging.debug("Checking : " + evry_file)
        file = open(evry_file)
        text = file.readlines()
        for line in text:
            check = searched_regex.search(line)
            if check is not None:
                print("Serched line is:\n " + line + "from file: " + evry_file)
                logging.debug("Find: " + line)
        file.close()
    logging.info("end")


regex, log_level = check_arg(sys.argv[1:])
print("The searched regex is: " + regex)
logging.basicConfig(filename='myProgramLog.txt', level=LOGGING[log_level],
                    format='%(asctime)s - %(levelname)s - %(message)s')
searched_regex = re.compile(regex)
search_for_regex(searched_regex)
