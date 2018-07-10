#!/usr/bin/env python3
"""Selective copy exercise"""

import os
import shutil
import argparse


def main():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path to source folder',
                        default='.\\test_tree_copy')
    parser.add_argument('--dst', help='Path to destination folder',
                        default='.\\new_folder')
    parser.add_argument('--ext', help='File extension',
                        default='.txt')
    args = parser.parse_args()

    if not os.path.exists(args.dst):
        os.mkdir(args.dst)

    for folder, _, files in os.walk(args.src):
        for file in files:
            if file.endswith(args.ext):
                shutil.copy(os.path.join(folder, file), args.dst)


if __name__ == '__main__':
    main()
