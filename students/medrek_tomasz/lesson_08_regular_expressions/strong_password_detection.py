#!/usr/bin/env python3


import re


def strong_password_detection(val_string):
    return True if re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.{8}).",
                            val_string) else False


def main():
    print(strong_password_detection("r4nyBoskie"))


if __name__ == "__main__":
    main()
