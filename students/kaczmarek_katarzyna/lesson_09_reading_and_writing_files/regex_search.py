import os
import re


def main():
    regex = re.compile(r'{}'.format(input("Enter regular expression: ")))
    for filename in os.listdir('.'):
        if filename.endswith(".txt"):
            with open(filename) as file:
                for line in file.readlines():
                    if regex.match(line):
                        print(line)


if __name__ == "__main__":
    main()
