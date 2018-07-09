import os
import re
import argparse
import logging


parser = argparse.ArgumentParser(description='Regex search')

parser.add_argument('-v', action='store',
                    dest='verbose', help='Verbose level - '
                                         'disabled, warning, info',
                    choices=['disabled', 'warning', 'info'])

parser.add_argument('-r', action='store',
                    dest="regex", required=True,
                    help='regex')

args = parser.parse_args()

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

if args.verbose == 'disabled':
    logging.disable(logging.CRITICAL)
elif args.verbose == 'warning':
    logging.getLogger().setLevel(logging.WARNING)
else:
    logging.getLogger().setLevel(logging.INFO)

text_files = []
logging.info('Looking for files with .txt extension')
for file in os.listdir('.'):
    if file.endswith(".txt"):
        logging.info('File: ' + file + ' found')
        text_files.append(file)

# regex = re.compile(r'\d{2}-\d{3}')
regex = re.compile(args.regex)

logging.info('Looking for line in all text files that match the regex')
for file in text_files:
    current_file = open(file)
    file_content = current_file.readlines()
    for line in file_content:
        mo = regex.search(line)
        if mo is not None:
            logging.info('Line found')
            print(line.strip())

    current_file.close()
logging.info('End')
