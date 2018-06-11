import sys
import re
import os
import argparse


def filling_in_the_gaps():
    parser = argparse.ArgumentParser(description='Gaps filling.')

    parser.add_argument(
        '--prefix', action="store",
        dest='prefix',
        default='spam')

    parser.add_argument(
        '--suffix', action="store",
        dest='suffix',
        default='.txt')

    parser.add_argument(
        '--folder_path', action="store",
        dest='folder_path',
        default=os.getcwd())

    results = parser.parse_args(sys.argv[1:])

    regex = re.compile(results.prefix + r'.*(\d{3})' + results.suffix)
    tab = []
    new = []
    for folder, subfolders, files in os.walk(results.folder_path):
        for file in files:
            search = re.search(regex, file)
            if search is not None:
                tab.append(file)
    tab = sorted(tab)

    for i in range(len(tab)):
        if i < 9:
            new.append(results.prefix + '00' + str(i + 1) + results.suffix)
        elif i >= 9 & i < 99:
            new.append(results.prefix + '0' + str(i + 1) + results.suffix)
        else:
            new.append(results.prefix + str(i + 1) + results.suffix)

    for i in range(len(tab)):
        if new[i] != tab:
            os.replace(tab[i], new[i])


def main():
    filling_in_the_gaps()


if __name__ == "__main__":
    main()
