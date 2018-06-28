#!/usr/bin/env python3

import glob
import re


def main():
    regex = str(input("Give regex (for example .*) to be searched: "))
    print("Searching for following regex in all .txt files: " + regex)
    pattern = re.compile(regex)

    for path in glob.glob("*.txt"):
        file = open(path, "r")
        for line in file:
            if pattern.match(line):
                print("line:\n" + line + "from file: " + path + " matches!\n")


if __name__ == "__main__":
    main()
