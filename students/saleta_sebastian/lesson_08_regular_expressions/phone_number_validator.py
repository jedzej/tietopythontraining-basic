import re


def check_phone_number(phone_number):
    phone_regex = re.compile(r'^(\+\d{2}[- ]?)?(\d{3}[- ]?)(\d{3}[- ]?)\d{3}')
    if not phone_regex.match(phone_number):
        print("Invalid phone number")
        return False

    print("Valid phone number")
    return True


def main():
    user_phone_number = input('Please input phone number: ')
    print(check_phone_number(user_phone_number))


if __name__ == '__main__':
    main()
