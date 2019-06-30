'''
Email validator - write email validator
that checks if supplied string
is valid e-mail address
'''
import re


def validate_email(email):
    emailRule = re.compile(r'''
    ^([a-zA-Z_%+-]+      # username
    [a-zA-Z0-9_%+-]*
    \.?
    [a-zA-Z0-9_%+-]*)
    (@)                      # @ symbol
    ([a-zA-Z0-9.-]+)         # domain name
    (\.[a-zA-Z]{2,4})$      # dot-something
    ''', re.VERBOSE)
    res = emailRule.findall(email)
    if (res != []):
        print(email, "is valid")
    else:
        print(email, "is invalid")


if __name__ == "__main__":
    validate_email("jan.kowalski@gmail.com")
    validate_email("jan.kowalskigmail.com")
    validate_email("jan.kowalski@gmail")
    validate_email("jan.1kowalski@gmail.com")
    validate_email("1jan.kowalski@gmail.com")
    validate_email("1jan...kowalski@gmail.com")
    validate_email("jan...kowalski@gmail.com")
    validate_email("jankowalski@gmail.com")
    validate_email("jan kowalski@gmail.com")
    validate_email("jankowalski@poczta.wp.pl")
