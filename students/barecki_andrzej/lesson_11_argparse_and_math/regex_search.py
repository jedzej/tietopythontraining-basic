"""Modify project Regex Search from lesson 9 to use argparse
 for parsing input"""

import os
import re
import argparse
import datetime
import sys


def create_example_test_files(path, source_folder_param):
    index = 100
    os.chdir(path)
    print('Current working folder ', os.getcwd() + os.linesep)
    src_dir = ""

    """Create source folder(extend date/time approach)"""
    if source_folder_param is not None:
        if os.path.exists(source_folder_param):
            random_folder = os.path.join(source_folder_param + '_' +
                                         str(datetime.datetime.now().date()) +
                                         '_' + str(datetime.datetime.now().
                                                   time()).replace(':', '.'))
            src_dir = random_folder
        else:
            src_dir = source_folder_param

    """ Create example of few files """
    file_list = [os.path.join(src_dir, "file_1.txt"),
                 os.path.join(src_dir, "file_2.txt"),
                 os.path.join(src_dir, "file_3.txt"),
                 os.path.join(src_dir, "file_4.txt"),
                 os.path.join(src_dir, "file_5.txt"),
                 os.path.join(src_dir, "file_6.txt"),
                 os.path.join(src_dir, "file_7.txt"),
                 ]

    for elem in file_list:
        if not os.path.exists(os.path.dirname(elem)):
            os.makedirs(os.path.dirname(elem))
        with open(elem, "w") as test_file:
            index = index + 1
            test_file.write(str(index))
            test_file.close()

    return os.path.join(os.getcwd(), src_dir)


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='regex search helper'
                                                 ' for validate parameters')
    parser.add_argument('-r', '--regex',
                        help='regex user definition',
                        # required='True',
                        default='\d')
    parser.add_argument('-s', '--source',
                        help='source folder',
                        default='regex_search')
    results = parser.parse_args(args)
    return results.regex, results.source


def main():
    regex_param, source_param = check_arg(sys.argv[1:])

    path = create_example_test_files(os.getcwd(), source_param)
    print("Regex parameters is equal r'{0}'".format(regex_param))
    regex = re.compile(r'{}'.format(regex_param))
    for elem in os.listdir(path):
        if elem.lower().endswith('.txt'):
            input_file = open(os.path.join(path, elem), "r")
            content = input_file.readlines()
            for line in content:
                if regex.match(line):
                    print("Content: >>> {0} <<< in {1}".format(line, elem))


if __name__ == '__main__':
    main()
