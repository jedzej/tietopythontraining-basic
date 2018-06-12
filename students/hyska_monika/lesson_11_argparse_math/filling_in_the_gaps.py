"""
Program finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps
in the numbering (such as if there is a spam001.txt and spam003.txt but no
spam002.txt). Have the program rename all the later files to close this gap.
"""
import shutil
import os
import re
import argparse, sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Search files for selected'
                                                 'extension and copy to chose location')
    parser.add_argument('-p', '--path',
                        help='path to search files',
                        default='.')
    parser.add_argument('-pr', '--pefix',
                        help='search file with put prefix',
                        required='True')
    results = parser.parse_args(args)
    return (results.path,
            results.pefix)


def search_prefix_add_gaps(path, prefix_not_compiled):
    prefix = re.compile(prefix_not_compiled)
    number = 1
    for file_name in os.listdir(path):
        file_with_prefix = prefix.search(file_name)
        if file_with_prefix is None:
            continue
        print('File with prefix:', file_name)
        number_part = file_with_prefix.group(2)
        if (str(number).zfill(3)) != number_part:
            text_part = file_with_prefix.group(1)
            ext_part = file_with_prefix.group(3)
            new_file_name = text_part + (str(number).zfill(3)) + ext_part
            print('Changed file:', file_name, 'to:', new_file_name)
            shutil.move(os.path.join(path, file_name),
                        os.path.join(path, new_file_name))
        number += 1

"""
my_prefix = re.compile(r'(spam)(\d\d\d)(.txt)$')
search_prefix_add_gaps('.\\folder\\txt_files', my_prefix)

print('')
my_prefix = re.compile(r'(ada)(\d\d\d)(.doc)$')
search_prefix_add_gaps('.\\folder\\txt_files', my_prefix)

"""


def main():
    my_path, prefix = check_arg(sys.argv[1:])
    search_prefix_add_gaps(my_path, prefix)

if __name__ == '__main__':
    main()
