import os, re


def regex_search(reg):
    regex = re.compile(reg)
    files_list = os.listdir('.')

    for file in files_list:
        if file.endswith('.txt'):
            with open(file) as textfile:
                for line in textfile:
                    if regex.match(line):
                        print("Regex found " + line)


regex = input("Enter a regex: ")
regex_search(regex)
