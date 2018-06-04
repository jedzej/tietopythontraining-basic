import os
import shutil


def solve_conflicts(file_name, new_file, extension):
    copy_file_name = file_name
    while copy_file_name in os.listdir(new_file):
        copy_file_name = copy_file_name[:-len(extension)] + str(1) +\
                         extension
    return file_name


def make_selective_copy(file_extension, location):
    new_folder_path = location + '\\new_folder'
    for folders, subfolders, files in os.walk(location):
        if folders == new_folder_path:
            continue
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        for filename in files:
            if filename.endswith(file_extension):
                copy_file_name = solve_conflicts(filename, new_folder_path,
                                                 file_extension)
                shutil.copy(os.path.join(folders, filename),
                            os.path.join(new_folder_path, copy_file_name))


make_selective_copy('.pdf', 'C:\\Users\\wachumar\\Desktop')
