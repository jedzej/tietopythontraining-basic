import os
import shutil


file_type = ".jpg"
source = "/home/rybaapau/test"
destination = "/home/rybaapau/test_copy/"


def new_folder():
    new = destination
    if not os.path.exists(new):
        os.makedirs(new)


def selective_copy(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(file_type):
                filename_path = os.path.join(foldername, filename)
                shutil.copy(filename_path, destination)
                print('Copying ' + filename + ' to ' + destination)


if __name__ == '__main__':
    new_folder()
    selective_copy(source)
    print('The end')
