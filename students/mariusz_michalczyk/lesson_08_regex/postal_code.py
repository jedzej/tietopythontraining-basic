import re


def verify_postal_code(postal_code):
    regex = re.compile(r'\d{2}-\d{3}')
    matched = regex.search(postal_code)
    if matched:
        print("Valid")
    else:
        print("Not Valid")


if __name__ == '__main__':
    postal_code = input()
    verify_postal_code(postal_code)
