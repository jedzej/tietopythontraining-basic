import re


def email_validator(email):
    regex_email = re.compile(r'(^[a-zA-Z0-9.!#$%&\'*+\-/=?^_`{|}~]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if regex_email.match(email):
        return True
    return False


def main():
    emails = ("very.common@example.com", "x@example.com", "#!$%&'*+-/=?^_`{}|~@example.org", "a.pl", "a@pl")

    for email in emails:
        if email_validator(email):
            print(email + " is OK")
        else:
            print(email + " is not valid")


if __name__ == '__main__':
    main()
