import re


def validate_email(email):
    rgx_email = re.compile(r'[a-zA-Z0-9._%+-]+@[A-Za-z0-9]+(\.[a-zA-Z]{2,4})')
    matched = rgx_email.search(email)
    if matched is not None:
        print("Valid")
    else:
        print("Email is not valid")


if __name__ == '__main__':
    email = input("Enter email: ")
    validate_email(email)
