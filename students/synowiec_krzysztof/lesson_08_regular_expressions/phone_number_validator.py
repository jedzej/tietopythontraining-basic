import re


def main():
    phone = input("Provide phone number: ")
    if is_phone_valid(phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")


def is_phone_valid(phone):
    regex = re.compile(r'(\+\d{2}\s)?\d{3}[\s-]?\d{3}[\s-]?\d{3}')
    return regex.match(phone)


if __name__ == '__main__':
    main()
