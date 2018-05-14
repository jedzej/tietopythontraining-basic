import re


def phone_validator(phone_number):

    re_number = re.compile(r'''(\+\d{2})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})''')
    mo = re_number.search(phone_number)

    if mo != None:
        if mo.group() == phone_number:
            return True
        else:
            return False
    else:
        return False


test = input("Phone number:  ")
print(phone_validator(test))
