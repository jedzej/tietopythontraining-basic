# Write a function that uses regular expressions to make sure the password
# string it is passed is strong.  A strong password is defined as one that
# is at least eight characters long, contains both uppercase and lowercase
# characters, and has at least one digit. You may need to test the string
# against multiple regex patterns to validate its strength.


import re


def password_strength(pwd):
    pwd_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    mo = pwd_regex.search(pwd)

    if mo is None:
        print('Password too weak.')
    else:
        print(mo.group())


def main():
    password_strength(input())


if __name__ == "__main__":
    main()
