"""
Program walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.
"""
import shutil
import os
import argparse, sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Search files for selected'
                                                 'extension and copy to chose location')
    parser.add_argument('-p', '--path',
                        help='path to search files',
                        default='.')
    parser.add_argument('-dp', '--destination_path',
                        help='path to paste files',
                        required='True')
    parser.add_argument('-e', '--extension',
                        nargs='*',
                        help='to search file with put extension',
                        required = 'True')
    results = parser.parse_args(args)
    return (results.path,
            results.destination_path,
            results.extension)


# function search files on selected folder for selected extensions
# and paste files to new location
def copy_files_to_new_location2(path, paste_path, extensions):
    extensions = tuple(extensions)
    if not os.path.exists(paste_path):
        os.makedirs(paste_path)
    print('Copied files:')
    for folder_name, sub_folders, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith(extensions):
                if os.path.isfile(os.path.join(paste_path, file_name)):
                    continue
                else:
                    shutil.copy(os.path.join(folder_name, file_name), paste_path)
                    print(folder_name + '\\' + file_name +
                          "   -->   " + paste_path + '\\' + file_name)


def main():
    search_my_path, paste_path, extension = check_arg(sys.argv[1:])
    copy_files_to_new_location2(search_my_path, paste_path, extension)

if __name__ == '__main__':
    main()
