import os
import re
import random


TEST_FILES_DIRECTORY = 'spam_fill_gaps_files'
CORRECT_FILE_NAMES_DIRECTORY = 'fill_gaps_files'
FILE_NAME = 'spam'
TXT_EXTENSION = 'txt'


def create_test_data():
    if not os.path.exists(TEST_FILES_DIRECTORY):
        os.makedirs(TEST_FILES_DIRECTORY)

    # Create files with gaps
    for i in random.sample(range(2, 20), 5):
        open(os.path.join(TEST_FILES_DIRECTORY, "{}{:03d}.{}".format
                          (FILE_NAME, i, TXT_EXTENSION)), 'w')


def fill_the_gaps():
    start_number = 0
    for filename in sorted(os.listdir(TEST_FILES_DIRECTORY)):

        if re.match(r"{0}\d{{3}}.{1}$".format
                    (FILE_NAME, TXT_EXTENSION), filename):
            number_expected = start_number + 1
            correct_file_name = (FILE_NAME +
                                 '0' *
                                 (3 - len(str(number_expected))) +
                                 str(number_expected) + '.txt')
            if correct_file_name != filename:
                rename_file(filename, number_expected)

            start_number = number_expected


def rename_file(old_filename, index_file):
    old_path = os.path.join(TEST_FILES_DIRECTORY, old_filename)
    new_name = "{}{:03d}.{}".format(FILE_NAME, index_file, TXT_EXTENSION)
    new_path = os.path.join(TEST_FILES_DIRECTORY, new_name)
    os.rename(old_path, new_path)


def main():
    create_test_data()
    fill_the_gaps()


if __name__ == '__main__':
    main()
