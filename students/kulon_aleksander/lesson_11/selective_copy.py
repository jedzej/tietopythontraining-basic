import os
import shutil
import argparse
import sys
import fnmatch

path = '../lesson_11/testfolder/'
new_folder = 'new_folder'


def main():
    parser = argparse.ArgumentParser(description='Selective copy.')

    parser.add_argument(
        '-d', action="store",
        dest='new_folder',
        required=True)

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default=path)

    args = parser.parse_args(sys.argv[1:])
    if not os.path.exists(args.path + args.new_folder):
        os.makedirs(args.path + args.new_folder)

    for root, directory, files in os.walk(args.path):
        for file in files:
            if fnmatch.fnmatch(file, "*.jpg"):
                file_path = os.path.join(root, file)
                print(file_path)
                shutil.copy(file_path, args.path + args.new_folder)


if __name__ == "__main__":
    main()
