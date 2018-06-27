import shutil
import os
import re
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Give searched regex: ')
    parser.add_argument('-t', '--type',
                        help='"Give file type "',
                        default='txt')
    parser.add_argument('-d', '--destination',
                        help='"Give destination path "',
                        default='C:\\test1')
    parser.add_argument('-s', '--source',
                        help='"Give source path "',
                        default='C:\\test')

    results = parser.parse_args(args)
    return (results.type,
            results.destination,
            results.source)


type, destination, from_folder = check_arg(sys.argv[1:])
file_type = '^(.*?).' + type
searching_file_type = re.compile(file_type)

for folderName, subfolders, filenames in os.walk(from_folder):
    for filename in filenames:
        if re.search(searching_file_type, filename):
            source = folderName + '\\' + filename
            shutil.copy(source, destination)
