import re

regex = re.compile(r"^\d\d-\d\d\d$")


def postal_code_validator(some_postal_code):
    if regex.match(some_postal_code) is None:
        print("Incorrect postal code")
    else:
        print("Postal code is correct")


# postal_code_validator("12-222")
# postal_code_validator("333-22")
# postal_code_validator("1a-123")


user_code = input("Please enter the postal code: ")
postal_code_validator(user_code)
