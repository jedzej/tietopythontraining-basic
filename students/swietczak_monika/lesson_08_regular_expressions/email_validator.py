import re

regex = re.compile(r"[^@]+@[^@]+\.[^@]+")


def email_validator(some_email):
    if regex.match(some_email) is None:
        print("email is not valid")
    else:
        print("email is valid")


# email_validator("mail123@test.com")
# email_validator("mail.mail")
# email_validator("mail@test")


user_email = input("Please enter the email address: ")
email_validator(user_email)
