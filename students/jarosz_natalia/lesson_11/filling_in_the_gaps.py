import re
import os
import shutil
import argparse
import sys

PATH = '../lesson_11/test/'


def main():

    parser = argparse.ArgumentParser(description='Filling gaps.')

    parser.add_argument(
        '--pattern', action="store",
        dest='pattern',
        required=True)

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default=PATH)

    args = parser.parse_args(sys.argv[1:])

    sorted_numbers = []
    prefix_pattern = re.compile(r"{0}\d{{3}}".format(args.pattern))

    for folder_name, sub_folder, file_names in os.walk(args.path):
        for file_name in file_names:
            result = re.search(prefix_pattern, file_name)
            if result is not None:
                sorted_numbers.append(result.group(0).replace(
                                      args.pattern, ''))

    sorted_numbers = sorted(sorted_numbers)

    for i, value in enumerate(sorted_numbers):
        if str(i + 1).zfill(3) == value:
            continue

        next_one = str(i + 1).zfill(3)
        current = args.path + args.pattern + next_one + '.txt'
        nex_one = args.path + args.pattern + value + '.txt'
        if not os.path.isfile(current):
            shutil.move(nex_one, current)


if __name__ == "__main__":
    main()
