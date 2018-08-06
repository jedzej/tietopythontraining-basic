import os
import shutil


def selective_copy(source_folder, destination_folder, extension):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(extension):
                shutil.copy(os.path.join(source_folder, filename),
                            destination_folder)


source = r'C:\python_to_copy'
destination = r'C:\python_copied'
ext = '.txt'

if __name__ == '__main__':
    selective_copy(source, destination, ext)
