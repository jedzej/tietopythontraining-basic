"""
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no
spam002.txt). Have the program rename all the later files
to close this gap.

As an added challenge, write another program that can
insert gaps into numbered files so that a new file
can be added.
"""

import argparse
import os
import shutil
import sys


def args_parameters(args):
    parser = argparse.ArgumentParser(
        description='Copy only specific file format:')
    parser.add_argument('-p', '--path',
                        help="path to directory", default=os.getcwd())
    parser.add_argument('-r', '--relative',
                        help="Relative path to the directory", default="")
    parser.add_argument('-c', '--core',
                        help="Core part of the file names", required=True)

    result = parser.parse_args()

    return result.path, result.relative, result.core


path, relative, core_name_part = args_parameters(sys.argv)


def remove_gaps(directory, rel_path, prefix):
    if len(rel_path):
        directory = os.path.join(os.getcwd(), rel_path)
    files = os.listdir(directory)

    if len(files) == 0:
        return

    try:
        last_number = int(get_string_number(files[0], prefix))
    except ValueError:
        print("Oops! Something went wrong!")
        return

    for file_name in files:
        current_str_number = int(get_string_number(file_name, prefix))
        if current_str_number != last_number:
            src = os.path.join(directory, file_name)
            dst = os.path.join(directory,
                               prefix + '{0:03d}'.format(last_number + 1) +
                               get_extension(file_name))
            last_number += 1
            shutil.move(src, dst)


def get_string_number(file_name, prefix):
    ext = file_name.find(".")
    number = file_name[len(prefix):ext]
    return number


def get_extension(name):
    return name[name.find("."):]


def main():
    remove_gaps(path, relative, core_name_part)


if __name__ == '__main__':
    main()
