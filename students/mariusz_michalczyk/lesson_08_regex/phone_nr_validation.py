import re


def validate_phone_nr(nr):
    regex = re.compile(r'(\+\d{2})*\s*\-*(\d{3})\s*\-*(\d{3})\s*\-*(\d{3})')
    matched = regex.search(nr)
    if matched:
        print("Valid")
    else:
        print("Not Valid")


if __name__ == '__main__':
    nr = input()
    validate_phone_nr(nr)
