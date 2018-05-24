"""
Email validator - write email validator that checks
if supplied string is valid e-mail address
"""
import re


def check_email(email):
    if len(email) > 254:
        return False
    # simplified rules:
    mail_pattern = re.compile(r'(^[a-zA-Z]'
                              '[a-zA-Z0-9.!#$%&\'*+\-/=?^_`{|}~]+'
                              '@'
                              '[a-zA-Z0-9\-]+'
                              '\.'
                              '[a-zA-Z0-9/-]+'
                              '[a-zA-Z0-9]$)')
    return mail_pattern.match(email)


def main():
    print("Please input adress to check:")
    if check_email(input()):
        print("This is correct email adress")
    else:
        print("This is an incorrect email adress")


if __name__ == '__main__':
    main()
