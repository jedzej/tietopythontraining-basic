import re
import os
import logging
import argparse

parser = argparse.ArgumentParser(description='Fillings the gaps program')

parser.add_argument('-d',
                help="regex expression",
                regex='regex',
                required=True)

parser.add_argument('-v', '--verbose',
                help='log level',
                choices=['disabled', 'warning', 'info'],
                default='info')

args = parser.parse_args()

if args.verbose == 'disabled':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.verbose == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)

regex = args.regex
search_exp = re.compile(regex)

for files in os.listdir('.'):
    if files.endswith(".txt"):
        opened_file = open(files, 'r')
        for line in opened_file:
            if search_exp.match(line):
                looging.info("Found in " + files + "\n")

