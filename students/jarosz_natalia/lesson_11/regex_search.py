import os
import re
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Searching for regex within .txt files')
    parser.add_argument('-r', '--regex',
                        help='Regex to be searched',
                        required=True)

    args = parser.parse_args()
    user_reg = re.compile(r'{}'.format(args.regex))

    text_files = os.listdir('.')

    print('What do you want to search for?')

    string_regex = re.compile(user_reg)

    for file in text_files:
        if file.endswith(".txt"):
            open_file = open(file)
            read_file = open_file.readlines()
            line_iterator = 1
            for line in read_file:
                if string_regex.search(line) is not None:
                    print(line)
                line_iterator += 1
            open_file.close()


if __name__ == "__main__":
    main()
