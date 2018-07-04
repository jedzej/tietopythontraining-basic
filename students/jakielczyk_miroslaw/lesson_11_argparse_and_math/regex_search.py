import os
import re
import argparse
import sys


def collect_arguments(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic arg-parse')

    parser.add_argument('-F', '--folder_to_be_searched',
                        help='provide relative or absolute path to the searched folder',
                        default='..\\lesson_09_reading_and_writing_files\\folder_with_text_files')

    parser.add_argument('-R', '--regex_expr',
                        help='regex expr. that will be used, default is: \d{2}-\d{3}',
                        default='\d{2}-\d{3}')

    results = parser.parse_args(args)
    return (results.folder_to_be_searched,
            results.regex_expr)


def search_files_for_regex(folder_path, regex_expression):
    regex_search = re.compile(regex_expression)
    folder_content = os.listdir(folder_path)
    list_of_text_files = []
    for file_name in folder_content:
        if file_name.endswith(".txt"):
            list_of_text_files.append(file_name)

    for text_file in list_of_text_files:
        print('\n', text_file)
        operating_file = open(os.path.join(folder_path, text_file), 'r')
        try:
            list_of_text_lines = operating_file.readlines()
            for each_text_line in list_of_text_lines:
                print(regex_search.findall(each_text_line))
        finally:
            operating_file.close()


def main():
    folder_path, regex_expression = collect_arguments(sys.argv[1:])
    search_files_for_regex(folder_path, regex_expression)


if __name__ == "__main__":
    main()
