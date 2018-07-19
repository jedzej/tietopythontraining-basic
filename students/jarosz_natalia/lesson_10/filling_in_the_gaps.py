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
        #print("size ", len(sorted_numbers))
        if i == len(sorted_numbers):
            #print("last element, break")
            break

        next_number = str(i + 1).zfill(3)
        #print("i: ", i)

        for j in range(i, int(sorted_numbers[-1])):
            later_number = str(j + 1).zfill(3)
            later_file = PATH + PATTERN + later_number + '.txt'
            if os.path.isfile(later_file):
                #print("later file: ", later_file)
                break
            else:
                #print("not found: ", later_file)

        #print("next_number ", next_number)
        #print("later_number ", later_number)

        next_file = PATH + PATTERN + next_number + '.txt'
        later_file = PATH + PATTERN + later_number + '.txt'
        print("next_file ", next_file)
        print("later_file ", later_file)
        if not os.path.isfile(next_number):
            print("replace ", later_file, " with ", next_file)
            shutil.move(later_file, next_file)


if __name__ == "__main__":
    main()
