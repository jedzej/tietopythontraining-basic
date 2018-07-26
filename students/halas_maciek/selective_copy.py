import os
import shutil


DESTINATION_DIRECTORY = 'temp'
TEST_FILES_DIRECTORY = 'test_files'
EXT = ['.jpg', '.pdf', '.txt', '.jpeg']


def create_test_data():
    if not os.path.exists(DESTINATION_DIRECTORY):
        os.makedirs(DESTINATION_DIRECTORY)
    if not os.path.exists(TEST_FILES_DIRECTORY):
        os.makedirs(TEST_FILES_DIRECTORY)

    open(os.path.join(TEST_FILES_DIRECTORY, "test1.txt"), 'w')
    open(os.path.join(TEST_FILES_DIRECTORY, 'panda.jpg'), 'w')
    open(os.path.join(TEST_FILES_DIRECTORY, 'vid.txt'), 'w')
    open(os.path.join(TEST_FILES_DIRECTORY, 'python.pdf'), 'w')


def move_files():
    for root, dirs, files in os.walk(TEST_FILES_DIRECTORY):
        for file in files:
            if file.endswith(tuple(EXT)):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, DESTINATION_DIRECTORY)


def main():
    create_test_data()
    move_files()


if __name__ == '__main__':
    main()