#!/usr/bin/env python3
"""Deleting unneeded files exercise"""

import os
import sys


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print('Invalid number of parameters')
    else:
        path = sys.argv[1]
        if os.path.exists(path):
            print('Files bigger than 100MB:')
            for folder, _, files in os.walk(path):
                for file in files:
                    if os.path.getsize(os.path.join(folder, file)) > 100000000:
                        print(folder + file)
        else:
            print('Invalid path: ' + path)


if __name__ == '__main__':
    main()
