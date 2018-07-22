import re
import os
import shutil

PATTERN = 'spam'
PATH = '../lesson_10/test/'


def main():
    sorted_numbers = []
    prefix_pattern = re.compile(r"{0}\d{{3}}".format(PATTERN))

    for folder_name, sub_folder, file_names in os.walk(PATH):
        for file_name in file_names:
            result = re.search(prefix_pattern, file_name)
            if result is not None:
                sorted_numbers.append(result.group(0).replace(PATTERN, ''))

    sorted_numbers = sorted(sorted_numbers)

    for i, value in enumerate(sorted_numbers):
        if str(i + 1).zfill(3) == value:
            continue

        next_one = str(i + 1).zfill(3)
        current = PATH + PATTERN + next_one + '.txt'
        nex_one = PATH + PATTERN + value + '.txt'
        if not os.path.isfile(current):
            shutil.move(nex_one, current)


if __name__ == "__main__":
    main()
