import os
import re
import random


TEST_FILES_DIRECTORY = 'insert_gaps_files'
FILE_NAME = 'spam'
TXT_EXTENSION = 'txt'


def create_test_data():
    if not os.path.exists(TEST_FILES_DIRECTORY):
        os.makedirs(TEST_FILES_DIRECTORY)
    # Create files with gaps
    for i in random.sample(range(2, 20), 5):
        open(os.path.join(TEST_FILES_DIRECTORY,
                          "{}{:03d}.{}".format(FILE_NAME, i, TXT_EXTENSION)),
             'w')


def insert_file_in_gap():
    gap_index = []
    for filename in sorted(os.listdir(TEST_FILES_DIRECTORY)):
        if re.match(r"{0}\d{{3}}.{1}$".format(FILE_NAME, TXT_EXTENSION),
                    filename):
            print(filename)
            index_regex = re.compile(r'[1-9][0-9]{0,1}')
            mo = index_regex.search(filename).group(0)
            if mo:
                gap_index.append(int(mo))

    insert_file(list(find_gaps(gap_index)))


def find_gaps(ids):
    """Generate the gaps in the list of file ids."""
    j = 1
    for id_i in sorted(ids):
        while True:
            id_j = int('%d' % j)
            j += 1
            if id_j >= id_i:
                break
            yield id_j


def insert_file(files_ids):
    for index_file in files_ids:
        open(os.path.join(TEST_FILES_DIRECTORY,
                          "{}{:03d}.{}".format(FILE_NAME, index_file,
                                               TXT_EXTENSION)), 'w')


def main():
    create_test_data()
    insert_file_in_gap()


if __name__ == '__main__':
    main()
