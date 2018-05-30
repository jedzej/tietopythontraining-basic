"""
Email validator
- email validator that checks if supplied string is valid e-mail address
correct emails:
    anaddd@gmail.com
    a@gmail.com
    432423@gmail.pl
    AnsSisfd.sf78767sa@gmail.coma
    anaddd@gmaxxxxxxxxxxil.com
- tests: email_validator_pytest.py
"""
import re


def check_email(email):
    email_regex = re.compile(r'''
        [a-zA-Z0-9._%+-]+      # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        \.[a-zA-Z]{2,4}$       # dot and 2 - 4 letters
        ''', re.VERBOSE)
    email_result = email_regex.match(email)
    if email_result is not None:
        print("Email is valid.")
        return True
    else:
        print("Email isn't valid.")
        return False


def main():
    email = input('Put email:')
    check_email(email)


if __name__ == '__main__':
    main()
