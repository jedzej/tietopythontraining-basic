import re
import os
import shutil

pattern = 'spam00'
path = '../lesson_10/testfolder/'


def main():
    sorted_numbers = []
    prefix_pattern = re.compile('(?<={})\w+'.format(pattern))

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
