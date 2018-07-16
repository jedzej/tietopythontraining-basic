import re
import os
import shutil

pattern = 'spam'
path = '../lesson_10/test/'


def main():
    sorted_numbers = []
    prefix_pattern = re.compile(r"{0}\d{{3}}".format(pattern))

    for foldername, subfolder, filenames in os.walk(path):
        for filename in filenames:
            result = re.search(prefix_pattern, filename)
            if result is not None:
                sorted_numbers.append(result.group(0).replace(pattern, ''))

    sorted_numbers = sorted(sorted_numbers)

    for i in range(int(sorted_numbers[0]), int(sorted_numbers[-1]) - 1):
        next = str(i + 1).zfill(3)
        later = str(i + 2).zfill(3)
        print(next)
        print(later)

        next_file = path + pattern + next + '.txt'
        later_file = path + pattern + later + '.txt'
        print(next_file)
        print(later_file)
        if not os.path.isfile(next):
            shutil.move(later_file, next_file)


if __name__ == "__main__":
    main()
