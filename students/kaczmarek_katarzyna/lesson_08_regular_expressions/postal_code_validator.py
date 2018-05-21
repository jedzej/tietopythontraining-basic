import re


def validate_postal_code_pl(postal_code):
    regex = re.compile(r'^\d{2}-\d{3}$')
    return regex.match(postal_code) is not None


def main():
    postal_codes = ['55-011',
                    '98-270',
                    '12345',
                    '1-234',
                    '12-3',
                    '12-3456',
                    '123-456',
                    '12x-345']

    for postal_code in postal_codes:
        print("\"" + postal_code + "\" - ", end="")
        if validate_postal_code_pl(postal_code):
            print("Valid!")
        else:
            print("Invalid!")


if __name__ == "__main__":
    main()
