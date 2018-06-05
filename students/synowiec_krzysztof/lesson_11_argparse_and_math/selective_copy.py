import os
import shutil
import fnmatch
import sys
import argparse


def main():
    s, d, e = check_args(sys.argv[1:])
    for root, directory, files in os.walk(s):
        for file in files:
            if fnmatch.fnmatch(file, '*' + e):
                file_path = os.path.join(root, file)
                print(file_path)
                shutil.copy(file_path, d)


def check_args(args=None):
    parser = argparse.ArgumentParser(description='Selective copy')
    parser.add_argument('-s', '--source',
                        help='Source folder',
                        required=True)

    parser.add_argument('-d', '--destination',
                        help='Destination folder',
                        required=True)

    parser.add_argument('-e', '--extension',
                        help='File extension e.g: .txt',
                        required=True)

    result = parser.parse_args(args)
    return result.source, result.destination, result.extension


if __name__ == '__main__':
    main()
