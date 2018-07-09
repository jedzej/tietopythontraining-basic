import re
import os
import shutil

pattern = 'spam'
path = '../lesson_10/testfolder/'


def main():
    sorted_numbers = []
    prefix_pattern = re.compile(r"{0}\d{{3}}".format(pattern))

    for folder_name, sub_folder, file_names in os.walk(path):
        for file_name in file_names:
            result = re.search(prefix_pattern, file_name)
            if result is not None:
                sorted_numbers.append(result.group(0).replace(pattern, ''))

    sorted_numbers = sorted(sorted_numbers)

    for i in range(int(sorted_numbers[0]), int(sorted_numbers[-1]) - 1):
        current = str(sorted_numbers[i-1]).zfill(3)
        next = str(int(sorted_numbers[i-1]) + 1).zfill(3)
        later = str(int(sorted_numbers[i-1]) + 2).zfill(3)

        current_file = path + pattern + current + '.txt'
        next_file = path + pattern + next + '.txt'
        later_file = path + pattern + later + '.txt'
        if not os.path.isfile(next):
            shutil.move(later_file, next_file)


if __name__ == "__main__":
    main()
