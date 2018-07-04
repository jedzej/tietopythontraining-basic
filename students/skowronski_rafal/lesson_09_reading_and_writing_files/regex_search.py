import os
import re

if __name__ == '__main__':
    input_directory = input('Enter directory: ')

    if not os.path.exists(input_directory):
        raise ValueError('Given directory does not exist')

    if not os.path.isdir(input_directory):
        raise ValueError('Given directory is not a directory')

    regex_text = input('Enter regular expression: ')
    regex = re.compile(regex_text)

    text_files_paths = [
        directory for directory
        in os.listdir(input_directory) if directory.endswith('.txt')]

    for text_file_path in text_files_paths:
        with open(text_file_path, mode='r') as text_file:
            for line in text_file.readlines():
                if regex.match(line) is not None:
                    print(line)
