import os

folder = 'C:\\Users\\becccluk\\Documents\\pythontraining'

for folder_name, sub_folders, \
    file_names in os.walk(folder):
    print('Folder name: ' + folder_name)

    for sub_folder in sub_folders:
        print('Subfolder name: ' + sub_folder)
    for file_name in file_names:
        print('File name: ' + file_name)
    print('')
