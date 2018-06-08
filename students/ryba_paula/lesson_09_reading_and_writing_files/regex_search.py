import re
import os


def regex_search(reg):
    regex = re.compile(reg)
    files_list = os.listdir('.')

    for el in files_list:
        if el[-4:] == ".txt":
            with open(el) as infile:
                for line in infile:
                    if regex.match(line):
                        print("Matched! " + line)


def main():
    regex = str(input("Give a regex: "))
    regex_search(regex)


if __name__ == '__main__':
    main()
