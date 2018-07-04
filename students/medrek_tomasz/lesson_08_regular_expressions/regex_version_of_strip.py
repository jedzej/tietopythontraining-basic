#!/usr/bin/env python3


import re


def strip_regex(work_str, del_str=' '):
    return re.sub("^[{0}]+|[{0}]+$".format(del_str), '', work_str)


def main():
    print(strip_regex("function works very well, so much fun", "nuf"))


if __name__ == "__main__":
    main()
