import os
import shutil
import fnmatch


SOURCE_FOLDER = "original"
DESTINATION_FOLDER = "copy"
EXTENSION = "*.txt"


def main():
    for root, directory, files in os.walk(SOURCE_FOLDER):
        for file in files:
            if fnmatch.fnmatch(file, EXTENSION):
                file_path = os.path.join(root, file)
                print(file_path)
                shutil.copy(file_path, DESTINATION_FOLDER)


if __name__ == '__main__':
    main()
