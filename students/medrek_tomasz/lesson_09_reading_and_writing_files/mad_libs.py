#!/usr/bin/env python3


import sys
import os


def print_usage():
    print("Usage: mad_lips.py <path to file>"
          ", you can enter path with prompt as well")


def main():
    string_from_file = ""
    argc = len(sys.argv)

    if argc > 1:
        file_path = sys.argv[1]
    else:
        print_usage()
        file_path = input('Please enter valid path to file:\n')

    if not os.path.isfile(file_path):
        print("File not found")
        exit()

    fh = open(file_path, 'r')
    string_from_file = fh.read()
    fh.close()

    key_words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    for key_word in key_words:
        if key_word in string_from_file:
            replace_word = input("Please enter {}:\n".format(key_word.lower()))
            string_from_file = string_from_file.replace(key_word, replace_word)

    dir_path, file_name = os.path.split(file_path)

    fh = open(os.path.join(dir_path, "new_{}".format(file_name)), 'w+')
    fh.write(string_from_file)
    fh.close()

    print(string_from_file)


if __name__ == "__main__":
    main()
