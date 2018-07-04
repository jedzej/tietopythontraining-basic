#!/usr/bin/env python3
"""Regexp exercise
"""

import os
import re
import argparse


def main():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--path',  help='Path to search location',
                        default='.\\txt_files')
    parser.add_argument('--regex',  help='Regex to search',
                        default='\d{2}')

    args = parser.parse_args()

    path = args.path
    pattern = re.compile(args.regex)
    if os.path.exists(path) and pattern:
        files = [file for file in os.listdir(path) if
                 file.endswith('.txt')]
        for f_name in files:
            file = open(os.path.join(path, f_name))
            for idx, line in enumerate(file.readlines()):
                match = pattern.search(line)
                if match:
                    print('Match: file: {0} line {1}'.
                          format(f_name, idx + 1))
            file.close()
    else:
        print("Invalid parameters")


if __name__ == '__main__':
    main()
