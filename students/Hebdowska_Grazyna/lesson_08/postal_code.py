import re


def postal_code_validator(code_number):

    re_number = re.compile(r'''((\d{2})(\s|-|\.)(\d{3}))''')
    mo = re_number.search(code_number)

    if mo is not None:
        print(mo.group())
        return True
    else:
        return False


test = input("Postal code:  ")
print(postal_code_validator(test))
