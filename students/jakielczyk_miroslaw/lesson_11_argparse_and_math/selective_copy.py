import os
import shutil
import argparse
import sys


def create_empty_folder(folder):
    if os.path.exists(folder):
        print('Removing', folder)
        shutil.rmtree(folder)
    print('Creating ', folder)
    os.makedirs(folder)


def collect_arguments(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic arg-parse')

    parser.add_argument('-R', '--root_folder',
                        help='provide relative or absolute path to the root folder',
                        default='..\\lesson_10_organizing_files\\folder_1')

    parser.add_argument('-D', '--destination_folder',
                        help='provide relative or absolute path to the destination folder',
                        default='target_folder')

    parser.add_argument('-F', '--files_type_ext',
                        type=str,
                        nargs='+',
                        help='provide files type extension, example: .jpg .pdf .txt',
                        default=['.pdf', '.jpg'])

    results = parser.parse_args(args)

    return (results.root_folder,
            results.destination_folder,
            results.files_type_ext)


def copy_files(root_folder, destination_folder, files_type_ext):
    for folder_name, sub_folders, file_names in os.walk(root_folder):
        print('\nFolder: %s...' % folder_name)
        for filename in file_names:
            for file_type_ext in files_type_ext:
                if filename.endswith(file_type_ext):
                    print('Copied file -> ', filename)
                    shutil.copy(os.path.join(folder_name, filename), destination_folder)


def main():
    root_folder, destination_folder, files_type_ext = collect_arguments(sys.argv[1:])
    create_empty_folder(destination_folder)
    print('Current folder ', os.getcwd())
    copy_files(root_folder, destination_folder, files_type_ext)


if __name__ == "__main__":
    main()
