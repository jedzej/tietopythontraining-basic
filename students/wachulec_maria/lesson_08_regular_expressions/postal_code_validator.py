import re


def postal_code_validator(text):
    postal_code_regex = re.compile(r'(\d{2})(\s|-)(\d{3})')
    try:
        if text == postal_code_regex.search(text).group(0):
            return 'Valid postal code'
    except AttributeError:
        return 'Invalid postal code'
    else:
        return 'Invalid postal code'


postal_code = '58-010'
print(postal_code_validator(postal_code))
