import os
import re
import argparse


def check_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix",
                        help="prefix",
                        default="spam")
    parser.add_argument("-d", "--directory",
                        help="directory",
                        default=r"C:\Python36\gaps")
    results = parser.parse_args(args)
    return results.prefix, results.directory


def fill_the_gaps(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        filenames = sorted(filenames)
        index = 1
        new_filename = ""
        for filename in filenames:
            if pattern.match(filename):
                if index == 1:
                    new_filename = filename
                print(filename, new_filename, index)
                if filename != new_filename:
                    print(
                        "Lack of filename: " + new_filename + "\nFile " +
                        filename + " will be renamed.")
                    filename_path = os.path.join(foldername, filename)
                    new_filename_path = os.path.join(foldername, new_filename)
                    os.rename(filename_path, new_filename_path)
                new_filename = filename.replace(str(index), str(index + 1))
                index += 1


if __name__ == '__main__':
    prefix, directory = check_args()
    pattern = re.compile(prefix + r'.*(\d{3})')
    fill_the_gaps(directory)