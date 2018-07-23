import glob
import shutil
import sys
import os
import argparse


def create_folder(name_folder):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--folder_path', action="store",
        dest='folder_path',
        default=name_folder + "/")
    result = parser.parse_args(sys.argv[1:])

    if os.path.exists(result.folder_path):
        shutil.rmtree(result.folder_path)
    os.mkdir(result.folder_path)
    return result.folder_path


def search_for_jpg_and_txt(folder_path):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--pdf', action="store",
        dest='pdf',
        default=".pdf")
    parser.add_argument(
        '--txt', action="store",
        dest='txt',
        default=".txt")
    parser.add_argument(
        '--subfolders', action="store",
        dest='subfolders',
        default="./**/*")
    results = parser.parse_args(sys.argv[1:])

    for extension in (results.pdf, results.txt):
        for path in glob.glob(results.subfolders + extension, recursive=True):
            shutil.copy2(path, folder_path)


def main():
    search_for_jpg_and_txt(create_folder("new_folder"))


if __name__ == "__main__":
    main()
