#!/usr/bin/env python3


import re


def phone_number_validator(validate_string):
    return True if re.match(r"^(\+\d{2}[- ]?)?(\d{3}[- ]?){2}\d{3}$",
                            validate_string) else False


def main():
    print(phone_number_validator("+48666666666"))


if __name__ == "__main__":
    main()
