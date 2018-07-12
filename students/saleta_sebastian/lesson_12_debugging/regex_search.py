import argparse
import logging
import os
import re
import sys


logging.basicConfig(level=logging.DEBUG, format=(' %(asctime)s - %(levelname)s'
                                                 ' - %(message)s'))
logger = logging.getLogger('__name__')


def set_logger_level(lvl):
    if lvl == 0:
        logging.disable(logging.CRITICAL)
    elif lvl == 1:
        logger.setLevel('WARNING')
    elif lvl == 2:
        logger.setLevel('INFO')


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to find sentence'
                                                 ' in txt files ')
    parser.add_argument('-p', '--sentence',
                        help='sentence to find in txt files',
                        required=True)
    parser.add_argument('-v', '--verbose',
                        help=('Verbose level.'
                              '0 - disabled, '
                              '1 - warnings and errors enabled '
                              '2 - info enabled'),
                        type=int)
    results = parser.parse_args(args)
    return results.sentence, results.verbose


def find_word_in_all_files(sentence):
    txt_files_index = 0
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            txt_files_index += 1
            with open(file) as reader:
                logger.info('Open file {}'.format(file))
                line_index = 0
                for line in reader:
                    line_index += 1
                    if re.search(r'{}'.format(sentence), line):
                        logger.info('Sentence found in file {}'.format(file))
                        logger.info('Sentence found in line {}'
                                    .format(line_index))
                        print('file : {}'.format(file))
                        print('line {}: {}'.format(line_index, line))
                    else:
                        logger.info('No sentences in file {}'.format(file))
                        print('Cannot find more sentences in files')

    if txt_files_index == 0:
        logger.warning('No .txt files in directory')


def main():
    user_sentence, verbose = check_arg(sys.argv[1:])
    set_logger_level(verbose)
    find_word_in_all_files(user_sentence)


if __name__ == '__main__':
    main()
