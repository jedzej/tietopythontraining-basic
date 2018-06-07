import re


def validate_phone_number(phone_number):
    regex = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    return regex.match(phone_number) is not None


def main():
    text = "123-123-123"
    print(text, "is valid phone number: ", validate_phone_number(text))


if __name__ == '__main__':
    main()
