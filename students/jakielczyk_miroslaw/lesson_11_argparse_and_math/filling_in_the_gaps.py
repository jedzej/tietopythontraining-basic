import os
import re
import shutil
import sys
import argparse

ORIGINAL_SPAM_FOLDER = '..\\lesson_10_organizing_files\\reference_spam_folder'


def collect_arguments(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic arg-parse')

    parser.add_argument('-F', '--source_folder_path',
                        help='provide either relative or absolute path to the source folder',
                        default='spam_folder')

    parser.add_argument('-P', '--prefix',
                        help='provide prefix of searched files',
                        default='spam')

    results = parser.parse_args(args)

    return (results.source_folder_path,
            results.prefix)


def filling_the_gaps(source_folder_path, prefix):
    file_index = 0
    regex_pattern = '^' + prefix + '\d{3}.txt$'
    regex_expression = re.compile(regex_pattern)

    for filename in os.listdir(source_folder_path):
        mo = regex_expression.search(filename)
        if mo is not None:
            file_index += 1

            correct_file_name = '{}{:03d}.txt'.format(prefix, file_index)

            if filename != correct_file_name:
                print(filename, '->', correct_file_name)
                shutil.move(os.path.join(source_folder_path, filename),
                            os.path.join(source_folder_path, correct_file_name))


def restore_content_of_source_folder(folder):
    if os.path.exists(folder):
        print('Removing content of spam_folder')
        shutil.rmtree(folder)
    print('Restoring original content of spam_folder')
    shutil.copytree(ORIGINAL_SPAM_FOLDER, folder)


def main():
    source_folder_path, prefix = collect_arguments(sys.argv[1:])
    restore_content_of_source_folder(source_folder_path)
    print('Current folder ', os.getcwd())
    filling_the_gaps(source_folder_path, prefix)


if __name__ == "__main__":
    main()
