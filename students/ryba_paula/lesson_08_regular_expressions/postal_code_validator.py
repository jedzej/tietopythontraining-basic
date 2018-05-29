import re


def postal_validator(code):
    regex_postal = re.compile(r'^\d{2}-\d{3}$')
    if regex_postal.match(code):
        return True
    return False


def main():
    codes = ("50-000", "iwiq", "49384", "02930", "38-333", "333-33", "1a-1a1")

    for code in codes:
        if postal_validator(code):
            print(code + " is OK")
        else:
            print(code + " is not valid")


if __name__ == '__main__':
    main()
