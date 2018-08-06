import re
import os
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Filling in the gaps')

    parser.add_argument('-p', '--prefix',
                        help='prefix',
                        default='spam')

    parser.add_argument('-s', '--suffix',
                        help='suffix',
                        default='.txt')

    parser.add_argument('-f', '--folder',
                        help='folder',
                        default='/home/user/Desktop/'
                                'lesson_11_argparse_and_math/')

    results = parser.parse_args(args)
    return (results.prefix,
            results.suffix,
            results.folder)


def filling_in_the_gaps():
    prefix, suffix, folder_path = check_arg(sys.argv[1:])
    regex = re.compile(prefix + r'.*(\d{3})' + suffix)
    tab = []
    new = []

    for folder, subfolders, files in os.walk(folder_path):
        for file in files:
            search = re.search(regex, file)
            if search is not None:
                tab.append(file)

    tab = sorted(tab)

    for i in range(len(tab)):
        new.append('{}{:03d}{}'.format(prefix, (i + 1), suffix))
    for i in range(len(tab)):
        if new[i] != tab:
            os.replace(tab[i], new[i])


def main():
    filling_in_the_gaps()


if __name__ == "__main__":
    main()
