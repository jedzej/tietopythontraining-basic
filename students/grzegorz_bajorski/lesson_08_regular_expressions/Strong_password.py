import re


def check_pwd(password):
    if len(password) <= 7:
        print("password should contain more than 8 characters")
        return False

    letters = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')
    if letters.search(password) is None:
        print("password should contain at least one digit")
        print(" and uppercase and lowercase letter")
        return False

    special_mark = re.compile(r'^(?=.*[!@#$%^&*()])')
    if special_mark.search(password) is None:
        print("password should contain at least one special char")
        return False
    return True


print("Provide password")
password = input(str())

if check_pwd(password):
    print("Password is strong")
