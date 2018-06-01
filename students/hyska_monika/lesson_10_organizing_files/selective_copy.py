"""
Program walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.
"""
import shutil
import os


# function search file on selected folder for selected extension
# (possible search for 2 extension in the same time)
# function return list found files
def search_files_list(path, ext1, ext2=None):
    files_list = []
    print('Found files:')
    for folder_name, sub_folders, file_names in os.walk(path):
        for file_name in file_names:
            if ext2 is None:
                if file_name.endswith(ext1):
                    print(folder_name + '\\' + file_name)
                    files_list.append(os.path.join(folder_name, file_name))
            else:
                if file_name.endswith(ext1) or file_name.endswith(ext2):
                    print(folder_name + '\\' + file_name)
                    files_list.append(os.path.join(folder_name, file_name))
    return files_list


# function search files on selected folder for selected extensions
def search_files_list2(path, *extensions):
    files_list = []
    print('Found files:')
    for folder_name, sub_folders, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith(extensions):
                print(folder_name + '\\' + file_name)
                files_list.append(os.path.join(folder_name, file_name))
    return files_list


# function copy files from list to new location
def copy_files_to_new_location(files_list, new_location):
    if not os.path.exists(new_location):
        os.makedirs(new_location)
    for file in files_list:
        if os.path.isfile(new_location):
            continue
        else:
            shutil.copy(file, new_location)


my_files_list = search_files_list2('.\\folder', '.pdf', '.JPG')
# my_files_list = search_files_list('.\\folder', '.pdf')
copy_files_to_new_location(my_files_list, 'new_folder')
