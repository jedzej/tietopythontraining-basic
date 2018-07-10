import os
import re

user_directory = 'C:\\Pajton'
name_pattern = re.compile(r'(.*[^1-9])(\d+)(.*[^1-9])')
names = []
correct_names = []
first_parts = []
digit_parts = []
proper_digit_parts = []
extension_parts = []


def list_files(given_folder):
    for files in os.listdir(given_folder):
        print(files)
        similar_name = name_pattern.search(files)
        try:
            if similar_name.group():
                names.append(similar_name.group())

        except AttributeError:
            print('No match')


def slice_filename(table):
    for i in range(0, len(table)):
        x = name_pattern.search(table[i])
        first_parts.append(x.group(1))
        digit_parts.append(int(x.group(2)))
        extension_parts.append(x.group(3))


def correct_numeration(table):
    table = sorted(table)
    for i in range(table[0], len(table) + table[0]):
        proper_digit_parts.append(i)


def format_new_names(begining, digits, extension):
    for i in range(len(digits)):
        print(begining[i] + str(digits[i]) + extension[i])
        # os.rename()


def run_program():
    print('Files: ')
    list_files(user_directory)
    slice_filename(names)
    correct_numeration(digit_parts)

    print()
    print('New names: ')
    format_new_names(first_parts, proper_digit_parts, extension_parts)


run_program()
