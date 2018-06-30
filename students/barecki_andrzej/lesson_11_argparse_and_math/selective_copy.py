"""Modify project Selective Copy from lesson 10 to use argparse for
parsing input"""

import os
import datetime
import shutil
import sys
import argparse


def create_example_file_tree(path, source_folder_param, des_folder_param):
    os.chdir(path)
    print('Current working directory folder ', os.getcwd())
    src_dir = ""

    """Create source folder(extend date/time approach)"""
    if source_folder_param is not None:
        if os.path.exists(source_folder_param):
            random_folder = os.path.join(source_folder_param + '_' +
                                         str(datetime.datetime.now().date()) +
                                         '_' + str(datetime.datetime.now().
                                                   time()).replace(':', '.'))
            src_dir = random_folder
        else:
            src_dir = source_folder_param

    """ Create example of few files """
    file_list = [os.path.join(src_dir, "dir_1", "test1.jpg"),
                 os.path.join(src_dir, "dir_1", "test2.pdf"),
                 os.path.join(src_dir, "dir_1", "test3.doc"),
                 os.path.join(src_dir, "dir_1", "dir_2", "test4.jpg"),
                 os.path.join(src_dir, "dir_1", "dir_2", "test5.pdf"),
                 os.path.join(src_dir, "dir_1", "dir_2", "test6.doc"),
                 os.path.join(src_dir, "dir_1", "dir_2", "dir_3", "test7.jpg"),
                 os.path.join(src_dir, "dir_1", "dir_2", "dir_3", "test8.pdf"),
                 os.path.join(src_dir, "dir_1", "dir_2", "dir_3", "test9.doc"),
                 ]
    for elem in file_list:
        if not os.path.exists(os.path.dirname(elem)):
            os.makedirs(os.path.dirname(elem))
        with open(elem, "w") as test_file:
            test_file.close()

    """Create destination folder(remove approach)"""
    if os.path.exists(des_folder_param):
        shutil.rmtree(des_folder_param)
    os.mkdir(des_folder_param)

    return os.path.join(os.getcwd(), src_dir)


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='selective_copy helper'
                                                 ' for validate parameters')
    parser.add_argument('-e', '--extension',
                        help='extension files',
                        default=['.pdf', '.jpg'])
    parser.add_argument('-s', '--source',
                        help='source folder',
                        default='source_selective_copy')
    parser.add_argument('-d', '--destination',
                        help='destination folder',
                        default='destination_selective_copy')
    results = parser.parse_args(args)
    return results.extension, results.source, results.destination


def main():
    extension_param, source_param, dest_param = check_arg(sys.argv[1:])

    source_path = create_example_file_tree(os.getcwd(), source_param,
                                           dest_param)
    destination_path = os.path.join(os.getcwd(), dest_param)

    for folder_name, _, file_names in os.walk(source_path):
        for filename in file_names:
            if filename.endswith(tuple(extension_param)):
                shutil.copy(os.path.join(folder_name, filename),
                            destination_path)


if __name__ == '__main__':
    main()
