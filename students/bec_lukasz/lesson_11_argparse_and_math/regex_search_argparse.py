import os
import re
import argparse


parser = argparse.ArgumentParser(description='Searching for matching regex')
parser.add_argument('-f', '--folder', action="store", type=str)
parser.add_argument('-r', '--regex', action="store", type=str)
arguments = parser.parse_args()

target_folder_path = arguments.folder
target_regex = re.compile(arguments.regex)

for file in os.listdir(target_folder_path):
    if '.txt' in file:
        txt_file = open(os.path.join(target_folder_path, file), 'r')
        content = txt_file.read()
        txt_file.close()
        result = target_regex.search(content)
        try:
            print(result.group())
        except AttributeError:
            print('Not found')


