#!/usr/bin/env python3
"""Regexp exercise
"""

import os
import re
import argparse
import logging

logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')


def main():
    """Main function"""

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Path to search location',
                        default='.\\txt_files')
    parser.add_argument('--regex', help='Regex to search',
                        default='\d{2}')
    parser.add_argument('--verbose', help='Regex to search',
                        choices=['disable', 'warning', 'info'],
                        default='info')

    args = parser.parse_args()

    if args.verbose == 'disable':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.verbose == 'warning':
        logging.getLogger().setLevel(logging.WARNING)

    path = args.path
    pattern = re.compile(args.regex)
    logging.info('Search for pattern %s in path %s', args.regex, path)
    if os.path.exists(path) and pattern:
        files = [file for file in os.listdir(path) if
                 file.endswith('.txt')]
        for f_name in files:
            file = open(os.path.join(path, f_name))
            for idx, line in enumerate(file.readlines()):
                match = pattern.search(line)
                if match:
                    logging.info('Match: file: %s line %s', f_name, idx + 1)
            file.close()
    else:
        logging.warning("Invalid parameters")


if __name__ == '__main__':
    main()
