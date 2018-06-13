import os
import re
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Regex search')

    parser.add_argument('directory',
                        help='Directory to search')
    parser.add_argument('file_match',
                        help='Regular expression to match file name')
    parser.add_argument('match',
                        help='Regular expression to match line')

    args = parser.parse_args()

    regex = re.compile(args.match)
    file_regex = re.compile(args.file_match)

    file_names = [
        file_name for file_name
        in os.listdir(args.directory)
        if file_regex.match(file_name) is not None]

    for file_name in file_names:
        file_path = os.path.join(args.directory, file_name)
        with open(file_path, mode='r') as text_file:
            for line in text_file.readlines():
                if regex.match(line) is not None:
                    print(line)
