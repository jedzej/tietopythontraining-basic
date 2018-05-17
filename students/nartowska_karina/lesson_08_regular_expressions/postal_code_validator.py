import re


def postal_code_validator(code):
    r_code = re.compile(r'^\d{2}-\d{3}$')
    if r_code.match(code):
        return 1


def main():
    set_of_postal_codes = ("text",
                           "email@email.com",
                           "12/345",
                           "123-45",
                           "12a-345b",
                           "12a-345",
                           "12-345b",
                           "59-430")
    for code in set_of_postal_codes:
        if postal_code_validator(code):
            print(code + " is postal code")


if __name__ == "__main__":
    main()
