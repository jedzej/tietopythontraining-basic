#!/usr/bin/env python3
"""Regexp exercise
    # Usage: py.exe mcb.pyw <path> <pattern>
"""

import os
import sys
import re


def main():
    """Main function"""

    if len(sys.argv) == 3:
        path = sys.argv[1]
        pattern = re.compile(sys.argv[2])
        if os.path.exists(path) and pattern:
            files = [file for file in os.listdir(path) if
                     file.endswith('.txt')]
            for f_name in files:
                file = open(path + f_name)
                for idx, line in enumerate(file.readlines()):
                    match = pattern.search(line)
                    if match:
                        print('Match: file: {0} line {1}'.
                              format(f_name, idx + 1))
                file.close()
        else:
            print("Invalid parameters")
    else:
        print('Invalid number of parameters')


if __name__ == '__main__':
    main()
