'''
Postal code validator - write postal code validator
that checks if supplied
'''
import re


def validate_postal_code(code):
    codeRule = re.compile(r'''
    ^(\d{2})    # firt two digit
    ([-]{1})    # hyphen
    (\d{3})$    # second trhee digit
    ''', re.VERBOSE)
    res = codeRule.findall(code)
    if (res != [] and len(res[0]) == 3):
        print(code, "is valid")
    else:
        print(code, "is not valid")


if __name__ == "__main__":
    validate_postal_code("50-382")
    validate_postal_code("50 382")
    validate_postal_code("50382")
    validate_postal_code("alama")
