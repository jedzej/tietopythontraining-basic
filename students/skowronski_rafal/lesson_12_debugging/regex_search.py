import os
import re
import argparse
import logging
import traceback


def configure_logger(verbosity_level):
    if verbosity_level == 'warning':
        level = logging.WARNING
    elif verbosity_level == 'info':
        level = logging.INFO
    else:
        logging.disable(level=logging.CRITICAL)
        return

    logging.basicConfig(level=level,
                        format='%(levelname)s - %(asctime)s - %(message)s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Regex search')

    parser.add_argument('directory',
                        help='Directory to search')
    parser.add_argument('file_match',
                        help='Regular expression to match file name')
    parser.add_argument('match',
                        help='Regular expression to match line')
    parser.add_argument('--verbosity', '-v',
                        choices=['disabled', 'warning', 'info'],
                        default='disabled', dest='verbosity_level',
                        help='Level of logging verbosity')

    args = parser.parse_args()
    configure_logger(args.verbosity_level)

    logging.info('Directory to search: {0}'.format(args.directory))
    logging.info('Regex pattern: {0}'.format(args.match))
    logging.info('File regex pattern: {0}'.format(args.file_match))

    try:
        regex = re.compile(args.match)
        file_regex = re.compile(args.file_match)
    except re.error:
        logging.critical('Invalid regex pattern.\n{0}'
                         .format(traceback.format_exc()))
        raise

    file_names = [
        file_name for file_name
        in os.listdir(args.directory)
        if file_regex.match(file_name) is not None]

    logging.info('Files to examine: {0}'.format(file_names))

    for file_name in file_names:
        file_path = os.path.join(args.directory, file_name)
        logging.info('File beeing examined: {0}'.format(file_path))
        try:
            with open(file_path, mode='r') as text_file:
                for line in text_file.readlines():
                    if regex.match(line) is not None:
                        print(line)
        except (IOError, FileNotFoundError) as error:
            logging.error(traceback.format_exc())
