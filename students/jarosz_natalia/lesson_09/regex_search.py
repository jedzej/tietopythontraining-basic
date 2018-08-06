import os
import re


def main():
    text_files = os.listdir('.')

    print('What do you want to search for?')
    user_reg = str(input())

    string_regex = re.compile(user_reg)

    for file in text_files:
        if file.endswith(".txt"):
            open_file = open(file)
            read_file = open_file.readlines()
            line_iterator = 1
            for line in read_file:
                if string_regex.search(line) is not None:
                    print(line)
                line_iterator += 1
            open_file.close()


if __name__ == "__main__":
    main()
