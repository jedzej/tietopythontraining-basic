import re

regex = re.compile(r"^\d{3}[- ]?\d{3}[- ]?\d{3}$")


def phone_number_validator(some_number):
    if regex.match(some_number) is None:
        print("Incorrect number")
    else:
        print("Correct number")


user_number = input("Please enter the phone number: ")
phone_number_validator(user_number)
