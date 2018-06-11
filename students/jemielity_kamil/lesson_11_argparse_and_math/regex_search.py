import os
import re
import argparse

parser = argparse.ArgumentParser(description='Regex search')
parser.add_argument('-r', action='store',
                    dest="regex", required=True,
                    help='regex')

args = parser.parse_args()

text_files = []

for file in os.listdir('.'):
    if file.endswith(".txt"):
        text_files.append(file)

# regex = re.compile(r'\d{2}-\d{3}')
regex = re.compile(args.regex)

for file in text_files:
    current_file = open(file)
    file_content = current_file.readlines()
    for line in file_content:
        mo = regex.search(line)
        if mo is not None:
            print(line.strip())

    current_file.close()
