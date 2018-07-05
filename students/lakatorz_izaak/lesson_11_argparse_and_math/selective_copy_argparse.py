import os
import shutil
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Gaps filling.')

    parser.add_argument(
        '-d', action="store",
        dest='new_dir',
        required='True')

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default='../lesson_11_argparse_and_math/')

    results = parser.parse_args(sys.argv[1:])

    if not os.path.exists(results.new_dir):
        os.makedirs(results.new_dir)

    for folder, subfolders, files in os.walk(results.path):
        for file in files:
            if file.endswith('.txt'):
                shutil.copy(file, '../' + results.new_dir)


if __name__ == '__main__':
    main()
