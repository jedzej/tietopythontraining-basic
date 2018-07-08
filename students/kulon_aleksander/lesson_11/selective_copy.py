import os
import shutil
import argparse
import sys

path = '../lesson_11/testfolder/'
new_folder = 'new_folder'


def main():
    parser = argparse.ArgumentParser(description='Selective copy.')

    parser.add_argument(
        '-d', action="store",
        dest='new_folder',
        required='True')

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default=path)

    results = parser.parse_args(sys.argv[1:])
    if not os.path.exists(path + new_folder):
        os.makedirs(path + new_folder)

    for root, directory, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, "*.jpg"):
                file_path = os.path.join(root, file)
                print(file_path)
                shutil.copy(file_path, path + new_folder)


if __name__ == "__main__":
    main()
