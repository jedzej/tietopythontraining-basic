#!/usr/bin/env python3

import re


def is_strong(password):
    strong = (len(password) >= 8 and
              re.compile(r'.*\d').match(password) and
              re.compile(r'.*\W|.*_').match(password) and
              re.compile(r'.*[A-Z]').match(password) and
              re.compile(r'.*[a-z]').match(password))

    if strong:
        print("Password: '" + password + "' is strong")
    else:
        print("Password: '" + password + "' is not strong")


def main():
    is_strong("icecream")
    is_strong("IceCream")
    is_strong("IceCream2")
    is_strong("IceCream2!")
    is_strong("Ice_Cream2")
    is_strong("2IceCream?")
    is_strong("i2C!")


if __name__ == "__main__":
    main()
