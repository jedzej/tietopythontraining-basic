"""
Program  walks in to a bar tree and searches for
exceptionally large files or folders, eg. size > 8 mb
Program delete found files and folders
"""
import shutil
import os


# function search folders and files bigger then some size
def search_files_folders_bigger_size(path, size):
    size_in_bytes = size * 1048576
    files_list = []
    folders_list = []
    find_files_folder_bigger(files_list, folders_list, path, size_in_bytes)
    print('Folders bigger then', size, 'mb:')
    print('\n'.join(map(str, folders_list)))
    print('Files bigger then', size, 'mb:')
    print('\n'.join(map(str, files_list)))
    return folders_list, files_list


def find_files_folder_bigger(files_list, folders_list, path, size_in_bytes):
    for folder_name, sub_folders, file_names in os.walk(path):
        folder_size = 0
        for file_name in file_names:
            file_name_with_path = os.path.join(folder_name, file_name)
            if os.path.getsize(file_name_with_path) > size_in_bytes:
                files_list.append(os.path.abspath(file_name_with_path))
            folder_size += os.path.getsize(file_name_with_path)
        if folder_size > size_in_bytes:
            folders_list.append(os.path.abspath(folder_name))


# function delete folders and file
def delete_to_big_folders_files(folders_list, files_list):
    for folder in folders_list:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    for file in files_list:
        if os.path.isfile(file):
            os.unlink(file)


search_files_folders_bigger_size('.\\folder', 0.05)

# --- you can check it after run selective_copy ---
# my_folders, my_files = search_files_folders_bigger_size('.\\new_folder', 8)
# delete_to_big_folders_files(my_folders, my_files)
