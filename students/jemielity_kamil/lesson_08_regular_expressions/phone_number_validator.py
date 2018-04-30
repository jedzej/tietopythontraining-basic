import re


def phone_validator(number):
    regex = re.compile(r'(\d{2}[- ]?)?((\d{3})[- ]?(\d{3})[- ]?(\d{3}))')
    mo = regex.search(number)
    if mo is not None:
        print(mo.group())
    else:
        print('Wrong phone number')


phone_validator('666-666-666')
phone_validator('666666666')
phone_validator('48-666-666-666')
phone_validator('666 666 666')
phone_validator('48 666 666 666')
