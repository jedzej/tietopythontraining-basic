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

    for i in range(int(sorted_numbers[0]), int(sorted_numbers[-1]) - 1):
        if i == len(sorted_numbers):
            break

        next_number = str(i + 1).zfill(3)

        for j in range(i, int(sorted_numbers[-1])):
            later_number = str(j + 1).zfill(3)
            later_file = PATH + PATTERN + later_number + '.txt'
            if os.path.isfile(later_file):
                break
            else:
                next_file = PATH + PATTERN + next_number + '.txt'
        later_file = PATH + PATTERN + later_number + '.txt'
        if not os.path.isfile(next_number):
            shutil.move(later_file, next_file)


if __name__ == "__main__":
    main()
