#!/usr/bin/env python3

import argparse
import glob
import os
import shutil
import sys


def check_arg(args):
    parser = argparse.ArgumentParser(description='Script for selectively copying files')
    parser.add_argument('-o', '--output_dir',
                        help='Output directory where copied files will be stored',
                        default="new_folder")
    parser.add_argument('-e', '--extension',
                        action='append',
                        help='File extension to be copied (e.g. txt)',
                        required=True)

    results = parser.parse_args(args)
    results.output_dir += "/"

    return results.output_dir, results.extension


def main():
    dir_path, extensions = check_arg(sys.argv[1:])
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)

    for extension in extensions:
        for path in glob.glob("./**/*" + extension, recursive=True):
            shutil.copy2(path, dir_path)


if __name__ == "__main__":
    main()
