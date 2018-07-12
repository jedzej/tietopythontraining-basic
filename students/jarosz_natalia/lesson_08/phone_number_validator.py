import re


def main():
    test_text = "666-666-666"
    print(test_text, "is valid phone number: ", phone_number(test_text))


def phone_number(number):
    regex = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    return regex.match(number) is not None


if __name__ == '__main__':
    main()
