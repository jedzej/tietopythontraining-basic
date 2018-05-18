import os
import re


def collect_arguments(folder_path, regex_expression):
    regex_search = re.compile(regex_expression)
    folder_content = os.listdir(folder_path)
    list_of_text_files = []
    for file in folder_content:
        if file.endswith(".txt"):
            list_of_text_files.append(file)

    for text_file in list_of_text_files:
        print('\n', text_file)
        file = open(os.path.join(folder_path, text_file), 'r')
        try:
            list_of_text_lines = file.readlines()
            for each_text_line in list_of_text_lines:
                print(regex_search.findall(each_text_line))
        finally:
            file.close()


def main():
    collect_arguments('folder_with_text_files', '\d{2}-\d{3}')


if __name__ == "__main__":
    main()
