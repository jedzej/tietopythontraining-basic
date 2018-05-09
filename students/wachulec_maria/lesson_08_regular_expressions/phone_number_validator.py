import re


def phone_number_validator(text):
    phone_regex = re.compile(r'\(?(\d{4}|\+\d{2})?\)?\d{9}')
    try:
        print(phone_regex.search(text).group(0))
        if text == phone_regex.search(text).group(0):
            return 'Valid phone number'
    except AttributeError:
        return 'Invalid phone number'
    else:
        return 'Invalid phone number'


number = '+43999999999'
print(phone_number_validator(number))
