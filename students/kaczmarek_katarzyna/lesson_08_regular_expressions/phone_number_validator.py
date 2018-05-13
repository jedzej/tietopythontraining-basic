import re


def validate_phone_number(phone_number):
    regex = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    return regex.match(phone_number) is not None


def main():
    phone_numbers = ['509704913',
                     '509 704 913',
                     '509-704-913',
                     '+48 509704913',
                     '+48509704913',
                     '+123 456 789 012',
                     '+1 509-704-913',
                     '50970491',
                     '+ 509704913',
                     '+509704913',
                     ' 509704913',
                     '509704913 ',
                     '5097O491Z',
                     '123-456',
                     '509-704- 913',
                     '+1234 12345678',
                     '509 704  913',
                     'xyz 555 shoe']

    for phone_number in phone_numbers:
        print(phone_number + " - ", end="")
        if validate_phone_number(phone_number):
            print("Valid!")
        else:
            print("Invalid!")


if __name__ == "__main__":
    main()
