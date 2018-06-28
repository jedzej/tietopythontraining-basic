import os
import re


def regex_search(reg):
    regex_text = re.compile(reg)
    files_list = os.listdir('.')

    for file in files_list:
        if file.endswith('.txt'):
            with open(file) as textfile:
                for line in textfile:
                    if regex_text.match(line):
                        print("Regex found " + line)


regex = input("Enter a regex: ")
regex_search(regex)
