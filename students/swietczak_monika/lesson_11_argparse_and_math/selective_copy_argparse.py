import os
import shutil
import argparse


def check_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source",
                        help="source directory",
                        default=r'C:\python_to_copy')
    parser.add_argument("-d", "--destination",
                        help="destination directory",
                        default=r'C:\python_copied')
    parser.add_argument("-e", "--extension",
                        help="extension",
                        default=".txt")
    results = parser.parse_args(args)
    return results.source, results.destination, results.extension


def selective_copy(source_folder, destination_folder, ext):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(ext):
                shutil.copy(os.path.join(source_folder, filename),
                            destination_folder)


if __name__ == '__main__':
    source, destination, extension = check_args()
    selective_copy(source, destination, extension)
