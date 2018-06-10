"""
Write a function that uses regular expressions to make
sure the password string it is passed is strong. A strong
password is defined as one that is at least eight
characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to
test the string against multiple regex patterns
to validate its strength.
"""
import re


def check_password(password):
    check_space = re.compile(r" *")
    password_no_white_space = check_space.sub('', password)
    if password != password_no_white_space:
        print("There shouldn't be any white spaces in the password")
        return False

    if len(password) < 8:
        print("Password is too short")
        return False

    if (re.compile(r".*[a-z]").match(password) and
            re.compile(r".*[A-Z]").match(password) and
            re.compile(r".*[0-9]").match(password)):
        return True
    return False


def main():
    print("Please input password to check:")
    if check_password(input()):
        print("This password is safe!")
    else:
        print("Password is not safe!")


if __name__ == '__main__':
    main()
