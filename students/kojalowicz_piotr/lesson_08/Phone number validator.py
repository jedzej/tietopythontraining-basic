import re


def validate_phone_number(value):
    rule = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    if rule.search(value):
        return True
    return False


print(validate_phone_number('99988877700'))
print(validate_phone_number('999 888 777'))
print(validate_phone_number('999-888-777'))
print(validate_phone_number('+48 999888777'))
print(validate_phone_number('+48999888777'))
print(validate_phone_number('+488 999 888 777'))
print(validate_phone_number('+4 999-888-777'))
