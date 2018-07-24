import re
import os
import argparse

parser = argparse.ArgumentParser(description='Fillings the gaps program')

parser.add_argument('-d',
                    help="regex expression",
                    regex='regex',
                    required=True)

args = parser.parse_args()

regex = args.regex
search_exp = re.compile(regex)

for files in os.listdir('.'):
    if files.endswith(".txt"):
        opened_file = open(files, 'r')
        for line in opened_file:
            if search_exp.match(line):
                print("Found in " + files + "\n")
