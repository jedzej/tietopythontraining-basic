#!/usr/bin/env python3


import re


def postal_code_validator_poland(validate_string):
    return True if re.match(r"^\d{2}-\d{3}$", validate_string) else False


def main():
    print(postal_code_validator_poland("43-370"))


if __name__ == "__main__":
    main()
