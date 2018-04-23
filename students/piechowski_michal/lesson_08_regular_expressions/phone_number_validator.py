#!/usr/bin/env python3

import re


def is_valid(phone_number):
    if re.compile(r'^\+').match(phone_number):
        prefix_size = 3
        if re.compile(r'.* |.*-').match(phone_number):
            prefix_size = 4

        prefix, phone_number = phone_number[:prefix_size], phone_number[prefix_size:]

        if not re.compile(r'^\+\d\d[ -]*$').match(prefix):
            return False

    if re.compile(r'^\d{9}$|^(\d{3}[ -]){2}\d{3}$').match(phone_number):
        return True

    return False


def main():
    potential_numbers = ("987654321", "123456789", "987 654 321",
                         "123-456-789", "+48987654321", "+48 987 654 321",
                         "+48-123-456-789", "+ab987654321", "+48+987654321",
                         "00-000", "iceCream", "12-345a")
    for phone_number in potential_numbers:
        if is_valid(phone_number):
            print("Phone number: " + phone_number + " is valid")
        else:
            print("Phone number: " + phone_number + " is not valid")


if __name__ == "__main__":
    main()