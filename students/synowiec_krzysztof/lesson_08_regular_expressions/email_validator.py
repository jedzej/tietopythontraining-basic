import re


def main():
    email = input("Provide email address: ")
    if is_email_valid(email):
        print("Valid email adress")
    else:
        print("invalid email adress")


def is_email_valid(email):
    regex = re.compile(r'[^@.\s][^@\s]+@[^@\s]+\.[^@\s]+')
    return regex.match(email)


if __name__ == '__main__':
    main()
