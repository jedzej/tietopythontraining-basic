import os
import re


def find_word_in_all_files(sentence):

    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            with open(file) as reader:
                line_index = 0
                for line in reader:
                    line_index += 1
                    if re.search(r'{}'.format(sentence), line):
                        print('file : {}'.format(file))
                        print('line {}: {}'.format(line_index, line))
                    else:
                        print('Cannot find more sentences in files')


def main():
    find_word_in_all_files(input())


if __name__ == '__main__':
    main()
