#!/usr/bin/env python3
"""Selective copy exercise"""

import os
import shutil


def main():
    """Main function"""
    dst_folder = 'new_folder/'
    if not os.path.exists(dst_folder):
        os.mkdir(dst_folder)

    for folder, _, files in os.walk('test_tree_copy'):
        for file in files:
            if file.endswith('.txt'):
                shutil.copy(os.path.join(folder, file), dst_folder)


if __name__ == '__main__':
    main()
