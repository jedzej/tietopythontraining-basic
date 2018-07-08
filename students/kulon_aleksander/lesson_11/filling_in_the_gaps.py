import re
import os
import shutil
import argparse
import sys

pattern = 'spam00'
path = '../lesson_11/testfolder/'


def main():
    sorted_numbers = []
    
    parser = argparse.ArgumentParser(description='Filling gaps.')

    parser.add_argument(
        '--pattern', action="store",
        dest='pattern',
        default=pattern,
        required='True')

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default=path)

    results = parser.parse_args(sys.argv[1:])

    prefix_pattern = re.compile('(?<={})\w+'.format(results.pattern))

    for folder_name, sub_folder, file_names in os.walk(path):
        for file_name in file_names:
            result = re.search(prefix_pattern, file_name)
            if result is not None:
                sorted_numbers.append(int(result.group(0)))

    sorted_numbers = sorted(sorted_numbers)

    for i in range(min(sorted_numbers), max(sorted_numbers)):
        test = path + pattern + str(i) + '.txt'

        if not os.path.isfile(test):
            shutil.move(path + pattern + str(i + 1) + '.txt', test)


if __name__ == "__main__":
    main()
