import re


def validate_phone_number():
    code = input("Type phone number: ")
    pattern = re.search(r'(\(\d{3}\)\s*\d{3}-\d{3}|\d{3}\d{3}\d{3}|\d{3}-\d{3}-\d{3})', code)
    if pattern:
        print("Correct phone number")
    else:
        print("Incorrect phone number")

validate_phone_number()
