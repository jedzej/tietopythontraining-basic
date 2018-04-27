# Postal code validator - write postal code validator that checks if supplied.

import re


def code_validator(code_str):
    code_regex = re.compile(r'^(\d{2}-\d{3})')
    mo = code_regex.search(code_str)

    if mo is None:
        print('Invalid postal code.')
    else:
        print(mo.group())


def main():
    code_validator('00-757 ')
    code_validator('15-5000')
    code_validator('155-530')


if __name__ == "__main__":
    main()
