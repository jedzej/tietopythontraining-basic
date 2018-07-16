import os
import shutil
import sys
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='selective copy')

    parser.add_argument('-s', '--source',
                        help='source folder',
                        required=True)

    parser.add_argument('-d', '--destination',
                        help='destination folder',
                        required=True)

    parser.add_argument('-e', '--extension',
                        help='file extension e.g: .pdf, .txt',
                        required=True)

    results = parser.parse_args(args)
    return (results.source,
            results.destination,
            results.extension)


def move_files(source_directory, destination_directory, extension):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(tuple(extension)):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, destination_directory)


def main():
    s, d, e = check_arg(sys.argv[1:])
    move_files(s, d, e)


if __name__ == '__main__':
    main()
