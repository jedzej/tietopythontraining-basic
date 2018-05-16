import re


def phone_number_validator(text):
    phone_regex = re.compile(r'\(?(\d{4}|\+\d{2})?\)?\s?'
                             r'(\d{9}|(\d{3}(\s|-)\d{3}(\s|-)\d{3}))')
    try:
        print(phone_regex.search(text).group(0))
        if text == phone_regex.search(text).group(0):
            return 'Valid phone number'
    except AttributeError:
        return 'Invalid phone number'
    else:
        return 'Invalid phone number'


number = '999-999-999'
print(phone_number_validator(number))
