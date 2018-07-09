import re
import os
import shutil
import argparse
import sys

path = '../lesson_11/testfolder/'


def main():
    sorted_numbers = []

    parser = argparse.ArgumentParser(description='Filling gaps.')

    parser.add_argument(
        '--pattern', action="store",
        dest='pattern',
        required=True)

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default=path)

    results = parser.parse_args(sys.argv[1:])

    prefix_pattern = re.compile(r"{0}\d{{3}}".format(results.pattern))

    for folder_name, sub_folder, file_names in os.walk(path):
        for file_name in file_names:
            result = re.search(prefix_pattern, file_name)
            if result is not None:
                sorted_numbers.append(result.group(0).replace(results.pattern,
                                                              ''))

    sorted_numbers = sorted(sorted_numbers)

    for i in range(int(sorted_numbers[0]), int(sorted_numbers[-1]) - 1):
        next = str(int(sorted_numbers[i - 1]) + 1).zfill(3)
        later = str(int(sorted_numbers[i - 1]) + 2).zfill(3)

        next_file = path + results.pattern + next + '.txt'
        later_file = path + results.pattern + later + '.txt'
        if not os.path.isfile(next):
            shutil.move(later_file, next_file)


if __name__ == "__main__":
    main()
