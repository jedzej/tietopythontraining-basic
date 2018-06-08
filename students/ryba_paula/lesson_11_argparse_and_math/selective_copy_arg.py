import os
import shutil
import argparse
import sys


def arg_input(args):
    parser = argparse.ArgumentParser(description="Selective copy program")
    parser.add_argument('-f', '--file_type', help="Filetype to be copied",
                        required=True)
    parser.add_argument('-s', '--source', help="Source dir",
                        default="/home/rybaapau/test")
    parser.add_argument('-d', '--destination', help="Destination dir",
                        default="/home/rybaapau/test_copy/")
    results = parser.parse_args(args)
    return results.file_type, results.source, results.destination


file_type, source, destination = arg_input(sys.argv[1:])


def new_folder():
    new = destination
    if not os.path.exists(new):
        os.makedirs(new)


def selective_copy(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(file_type):
                filename_path = os.path.join(foldername, filename)
                shutil.copy(filename_path, destination)
                print('Copying ' + filename + ' to ' + destination)


if __name__ == '__main__':
    new_folder()
    selective_copy(source)
    print('The end')
