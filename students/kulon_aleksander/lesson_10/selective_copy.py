import os
import shutil
import fnmatch

path = '../lesson_10/testfolder/'
new_folder = 'new_folder'


def main():
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
