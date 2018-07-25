import os
import re
import argparse


def check_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex",
                        help="regex",
                        default=".*")
    parser.add_argument("-d", "--directory",
                        help="directory",
                        default=r"C:\Python36\files")
    results = parser.parse_args(args)
    return results.regex, results.directory


def regex_search(reg, folder):
    regex_text = re.compile(reg)
    files_list = os.listdir(folder)
    for file in files_list:
        if file.endswith('.txt'):
            with open(os.path.join(folder, file)) as textfile:
                for line in textfile:
                    if regex_text.match(line):
                        print("Regex found " + line)


if __name__ == '__main__':
    regex, directory = check_args()
    regex_search(regex, directory)
