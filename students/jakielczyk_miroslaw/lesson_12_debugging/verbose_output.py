import os
import re
import argparse
import sys
import logging


def collect_arguments(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic arg-parse')

    parser.add_argument('-F', '--folder_to_be_searched',
                        help='provide relative or absolute path to the searched folder',
                        default='..\\lesson_09_reading_and_writing_files\\folder_with_text_files')

    parser.add_argument('-R', '--regex_expr',
                        help='regex expr. that will be used, default is: \d{2}-\d{3}',
                        default='\d{2}-\d{3}')

    parser.add_argument('-vo', '--verbose_output',
                        help='logging level, possible values: disabled, warning, info',
                        default='info')

    results = parser.parse_args(args)
    return (results.folder_to_be_searched,
            results.regex_expr, results.verbose_output)


def search_files_for_regex(folder_path, regex_expression):
    regex_search = re.compile(regex_expression)
    folder_content = os.listdir(folder_path)
    list_of_text_files = []
    for file_name in folder_content:
        if file_name.endswith(".txt"):
            list_of_text_files.append(file_name)
    if not list_of_text_files:
        logging.warning('There is no txt files in a folder')

    for text_file in list_of_text_files:
        logging.info('Text file -> ' + text_file)
        operating_file = open(os.path.join(folder_path, text_file), 'r')
        try:
            list_of_text_lines = operating_file.readlines()
            for each_text_line in list_of_text_lines:
                logging.info('Checked line -> ' + each_text_line.strip())
                print(regex_search.findall(each_text_line))
        finally:
            operating_file.close()


def main():
    logging_level = {'disabled': logging.CRITICAL, 'warning': logging.INFO, 'info': logging.DEBUG}
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

    folder_path, regex_expression, verbose_output = collect_arguments(sys.argv[1:])

    if verbose_output in logging_level:
        logging.disable(logging_level[verbose_output])
    else:
        logging.disable(logging.CRITICAL)

    if os.path.isdir(folder_path):
        search_files_for_regex(folder_path, regex_expression)
    else:
        logging.error('Given folder does not exist')


if __name__ == "__main__":
    main()
