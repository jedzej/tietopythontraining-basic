import os
import shutil

root_folder = 'folder_1'
destination_folder = 'target_folder'


def create_empty_folder(folder):
    if os.path.exists(folder):
        print('Removing', folder)
        shutil.rmtree(folder)
    print('Creating ', folder)
    os.makedirs(folder)


create_empty_folder(destination_folder)
print('Current folder ', os.getcwd())
for folder_name, sub_folders, file_names in os.walk(root_folder):
    print('\nFolder: %s...' % folder_name)
    for filename in file_names:
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            print('Copied file -> ', filename)
            shutil.copy(os.path.join(folder_name, filename), destination_folder)
