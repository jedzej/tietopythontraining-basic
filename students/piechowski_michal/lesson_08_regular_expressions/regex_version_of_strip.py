#!/usr/bin/env python3

import re


def my_strip(string_to_be_stripped, stripped_characters=" "):
    expression = "^([" + stripped_characters
    expression += "]*)|([" + stripped_characters + "]*)$"
    regex = re.compile(expression)
    print(regex.sub("", string_to_be_stripped))


def main():
    my_strip("  from default strip only spaces  ")
    my_strip("xxx  x'es can be stripped too xxxxxx", "x")
    my_strip("xYzxx even more characters could be stripped ZZZzzYxxx", "x Yz")


if __name__ == "__main__":
    main()
