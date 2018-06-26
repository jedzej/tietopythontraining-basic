import re


def validate_postal_code_pl(postal_code):
    regex = re.compile(r'^\d{2}-\d{3}$')
    return regex.match(postal_code) is not None


def main():
    text = "58-100"
    print(text, "is valid postal code: ", validate_postal_code_pl(text))


if __name__ == '__main__':
    main()
