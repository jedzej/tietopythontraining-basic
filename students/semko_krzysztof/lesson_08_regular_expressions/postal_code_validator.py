"""
Postal code validator - write postal code validator
that checks if supplied
"""
import re


def check_postal_code(code):
    if len(code) != 6:
        return False
    postal_pattern = re.compile(r"^[0-9]{2}-[0-9]{3}$")
    return postal_pattern.match(code)


def main():
    print("Please input a correct postal code:")
    if check_postal_code(input()):
        print("This is a correct postal code")
    else:
        print("This is not a correct postal code")


if __name__ == '__main__':
    main()
