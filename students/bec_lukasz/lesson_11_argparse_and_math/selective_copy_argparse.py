import os
import shutil
import argparse


parser = argparse.ArgumentParser(description='Copying selected type of files')


def find_args():
    parser.add_argument('-s', '--source', action="store", type=str)
    parser.add_argument('-e', '--extension', action="store", type=str)
    parser.add_argument('-f', '--folder', action="store", type=str)
    arguments = parser.parse_args()
    return arguments.source, arguments.extension, arguments.folder


def selective_copy(given_folder, given_extension, target_folder):
    folder = given_folder.replace(',', '')
    extension = given_extension.replace(',', '')

    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                shutil.copy(os.path.join(folder, filename),
                            target_folder)


def main():
    source, extension, folder = find_args()
    selective_copy(source, extension, folder)


if __name__ == '__main__':
    main()
