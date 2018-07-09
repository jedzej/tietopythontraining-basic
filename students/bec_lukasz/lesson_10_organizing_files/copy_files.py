import shutil
import os
import send2trash

for folder_name, sub_folders, file_names in os.walk('C:\\Users\\becccluk\\Documents\\pythontraining'):
    print('Folder name: ' + folder_name)

    for sub_folder in sub_folders:
        print('Subfolder name: ' + sub_folder)
    for file_name in file_names:
        print('File name: ' + file_name)
    print('')