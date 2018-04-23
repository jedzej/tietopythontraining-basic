#!/usr/bin/env python3

import re


def is_valid(postal_code):
    if re.compile(r'^\d{2}-\d{3}$').match(postal_code):
        return True

    return False


def main():
    potential_codes = ("Ice@Cream.com", "icecream", "000-000",
                       "00-000", "12-200", "12-345a",
                       "12a-345", "99-999", "87-654")
    for postal_code in potential_codes:
        if is_valid(postal_code):
            print("Postal code: " + postal_code + " is valid")
        else:
            print("Postal code: " + postal_code + " is not valid")


if __name__ == "__main__":
    main()