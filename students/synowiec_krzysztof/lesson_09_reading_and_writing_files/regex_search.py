import re
import os
import fnmatch
INPUT_FILE = 'input.txt'


def main():
    pattern = re.compile(r'{}'.format(input("Provide pattern: ")))
    txt_file_list = []
    for file in os.listdir(os.curdir):
        if fnmatch.fnmatch(file, "*.txt"):
            txt_file_list.append(file)

    for file in txt_file_list:
        with open(file) as reader:
            for line in reader:
                if re.match(pattern, line):
                    print(line)


if __name__ == '__main__':
    main()
