import os
import shutil


def selective_copy(given_folder, given_extension, target_folder):
    for folderName, subfolders, filenames in os.walk(given_folder):
        print('first')
        for filename in filenames:
            if filename.endswith(given_extension):
                shutil.copy(os.path.join(given_folder, filename),
                            target_folder)


selective_copy('C:\Pajton', '.txt', 'C:\Pajton\copy')
