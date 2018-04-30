import re


def postal_code_validator(code):
    regex = re.compile(r'\d{2}-\d{3}')
    mo = regex.search(code)

    if mo is not None:
        print('Postal code correct: ' + mo.group())
    else:
        print('Wrong postal code')


postal_code_validator('71-111')
postal_code_validator('1-1')
postal_code_validator('111-1')
postal_code_validator('string')
postal_code_validator('12-132')
