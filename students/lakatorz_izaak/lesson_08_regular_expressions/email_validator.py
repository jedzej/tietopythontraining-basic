# Email validator - write email validator that checks if supplied string is
# valid e-mail address.

import re


def email_validator(mail_str):
    mail_regex = re.compile(r'[a-zA-Z0-9._\-]+@[a-zA-Z0-9.\-]+\.\w{2,8}')
    mo = mail_regex.search(mail_str)

    if mo is None:
        print('Invalid email address.')
    else:
        print(mo.group())


def main():
    email_validator('j.smith@example.com.')
    email_validator('google.com@')


if __name__ == "__main__":
    main()
