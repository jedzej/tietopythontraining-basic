import os
import shutil
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Take extension and path")
    parser.add_argument('-e', '--extension', action='store_const',
                        const='.pdf', dest='file_extension', default='.txt',
                        help='Extension of file to copy')
    parser.add_argument('-p', '--path', dest='location',
                        help='Starting path of searching',
                        default=os.getcwd())
    results = parser.parse_args(args)
    return results.file_extension, results.location


def solve_conflicts(file_name, new_file, extension):
    copy_file_name = file_name
    while copy_file_name in os.listdir(new_file):
        copy_file_name = copy_file_name[:-len(extension)] + str(1) + extension
    return file_name


def make_selective_copy():
    file_extension, location = check_arg(sys.argv[1:])
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


make_selective_copy()
