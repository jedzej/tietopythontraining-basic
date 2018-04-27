# Phone number validator - write phone number validator that accepts phone
# numbers in not separated, space-separated or hypen-separated 9-digit
# format with optional country prefix.


import re


def phone_validator(phone_str):
    phone_regex = re.compile(
        r'([0-9]{1,3}-)?((\d{3})(-| )?(\d{3})(-| )?(\d{3}))')

    mo = phone_regex.search(phone_str)

    if mo is None:
        print('Invalid phone number.')
    else:
        print(mo.group())


def main():
    phone_validator('009-757-999')
    phone_validator('00-155000999')
    phone_validator('555 730 444')


if __name__ == "__main__":
    main()
