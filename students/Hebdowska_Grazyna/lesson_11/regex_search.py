import re
import glob
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Give searched regex: ')
    parser.add_argument('-q', '--question',
                        help='"Give searched regex: "',
                        default='/d/d/d')

    results = parser.parse_args(args)
    return results.question


def search_for_regex(searched_regex):
    for evry_file in glob.glob("*.txt"):
        file = open(evry_file)
        text = file.readlines()
        for line in text:
            check = searched_regex.search(line)
            if check is not None:
                print("Serched line is:\n " + line + "from file: " + evry_file)
        file.close()


regex = check_arg(sys.argv[1:])
print("The searched regex is: " + regex)
searched_regex = re.compile(regex)
search_for_regex(searched_regex)
