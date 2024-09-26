import re


def validate_code(code):
    code_regex = re.compile(r'[0-9]{2}-[0-9]{3}')
    match_code = code_regex.search(code)
    try:
        match_code.group()
        return 'Valid postal code: ' + code
    except AttributeError:
        return 'Not valid postal code: ' + code


print(validate_code('111'))
print(validate_code('10-111'))
print(validate_code('10-001'))
print(validate_code('10111'))
