import re

"""
1. At least 8 characters long
2. contains both uppercase and lowercase characters
3. at least one digit
"""


def pass_checker(some_password):
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$',
                some_password) is None:
        print("Password is not strong")
    else:
        print("Password is strong")


# pass_checker("abrakadabra")
# pass_checker("Abr4kadabra")
# pass_checker("123Test")
# pass_checker("1234Test")


user_password = input("Please enter a password: ")
pass_checker(user_password)
