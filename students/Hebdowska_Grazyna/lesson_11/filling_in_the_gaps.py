import os
import re
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Give searched regex: ')
    parser.add_argument('-s', '--source',
                        help='"Give source path "',
                        default='C:\\test1')

    results = parser.parse_args(args)
    return results.source


searching_file = re.compile(r"""spam(\d\d\d).txt""")
from_folder = check_arg(sys.argv[1:])

index = 0

for folderName, subfolders, filenames in os.walk(from_folder):
    for filename in sorted(filenames):
        if re.search(searching_file, filename):
            index += 1
            old_file = folderName + '\\' + filename
            new_file =\
                folderName + '\\' + 'spam' + str(index).zfill(3) + '.txt'
            os.rename(old_file, new_file)
