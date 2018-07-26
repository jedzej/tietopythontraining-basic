'''
Write a program that opens all .txt files in a folder
and searches for any line that matches a user-supplied
regular expression. The results should be printed to the screen.
'''
# ! python3
# regex_search.py - searche all .txt files
# for user specified regular expression
# Usage: py.exe regex_search.py <regular_expresion> <dir_path>
#   <regular_expresion> - specifies regular expression,
#   <dir_path>          - path to txt. files if not specified then
#                         current dir are searched

import sys
import os
import re


def print_usage():
    print("Usage: py.exe regex_search.py <regular_expresion> <dir_path>")
    print("<regular_expresion> - specifies regular expression,")
    print("<dir_path>          - path to txt. files, if not specified then")
    print("                      files from current dir are searched")


def regex_search():
    path_to_files = '.'
    search_rule = ''
    if len(sys.argv) == 3:
        path_to_files = sys.argv[2]
        search_rule = sys.argv[1]
    elif len(sys.argv) == 2:
        search_rule = sys.argv[1]
    else:
        print_usage()
        return
    try:
        for file_name in os.listdir(path_to_files):
            try:
                if file_name.endswith(".txt"):
                    print("Searching file: ", file_name)
                    text_file = open(file_name)
                    content = text_file.read()
                    regex_rule = re.compile(search_rule)
                    res = regex_rule.findall(content)
                    print(res)
            except FileNotFoundError as e:
                print("FileNotFoundError: " + str(e))
    except PermissionError:
        print("PermissionError")


if __name__ == "__main__":
    regex_search()
