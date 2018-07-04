import re


def phone_validator(number):
    regex_phone = re.compile(r'^(\+\d\d[ -]?)?'
                             '\d{3}(([ -]?\d{3}){2}$|([ -]?\d{2}){3}$)')

    if regex_phone.match(number):
        return True
    return False


def main():
    numbers = ("123456789", "123 456 789", "123-456-789", "+11123456789",
               "+11 123 456 789", "+11 123456789", "+11 123-456-789",
               "+11-123-456-789", "123 45 67 89", "+11 123 45 67 89",
               "123-45-67-89", "+11 123-45-67-89", "amam", "1234567890",
               "+11 +11 123456789", "+11 11 123456789", "11 123 45 67 89")

    for number in numbers:
        if phone_validator(number):
            print(number + " is OK")
        else:
            print(number + " is not valid")


if __name__ == '__main__':
    main()
