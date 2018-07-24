import re

def check_an_valid_email():
    email_to_check = input("Type an email to verify: ")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email_to_check)
    if match:
        print("Correct email")
    else:
        print("Incorrect email")

check_an_valid_email()