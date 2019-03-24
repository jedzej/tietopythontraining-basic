import re


def phone_validator(phone_number):
    s = r'(\+\d{2})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})'
    re_number = re.compile(s)
    mo = re_number.search(phone_number)
    if mo is not None:
        if mo.group() == phone_number:
            return True
        else:
            return False
    else:
        return False


test = input("Phone number:  ")
print(phone_validator(test))
