import os
import re

target_folder_path = input('Enter target folder path: ')
target_folder = os.listdir(target_folder_path)
target_regex = re.compile(r'(\w+)(@)(\w+)(\.{1})(\w+)')

for file in target_folder:
    if '.txt' in file:
        txt_file = open(os.path.join(target_folder_path, file), 'r')
        content = txt_file.read()
        txt_file.close()
        result = target_regex.search(content)
        try:
            print(result.group())
        except AttributeError:
            print('Not found')
