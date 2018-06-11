import os
import re
import sys
import argparse


files = []
parser = argparse.ArgumentParser()

parser.add_argument(
    '--txt', action="store",
    dest='txt',
    default=".txt")
result = parser.parse_args(sys.argv[1:])

for file in os.listdir(os.getcwd()):
    if file.endswith(result.txt):
        files.append(file)

regex = re.compile(r'\d{2}-\d{3}')

for file in files:
    current_file = open(file)
    file_content = current_file.readlines()
    for line in file_content:
        mo = regex.search(line)
        if mo is not None:
            print(line.strip())
    current_file.close()
