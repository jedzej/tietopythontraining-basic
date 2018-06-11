import re


def is_phone_valid(phone):
    r = re.compile(r'((\+\d{2})?\d{3}(\s|-)?\d{3}(\s|-)?\d{3})')
    s = r.search(phone)
    if s is None:
        return False
    print(s.group())
    return True


assert is_phone_valid('+48-500-123-222') is True
assert is_phone_valid('500-123-222') is True
assert is_phone_valid('500123222') is True
assert is_phone_valid('500 123 222') is True
assert is_phone_valid('+48500123222') is True

assert is_phone_valid('00 123 222') is False
assert is_phone_valid('00123222') is False
assert is_phone_valid('111 222 33') is False
assert is_phone_valid('111 222 33') is False
assert is_phone_valid('AAA BBB CCC') is False
