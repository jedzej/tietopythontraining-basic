import re


def check_strong(password):

    re_number1 = re.compile(r'((\w[a-z])+)')
    re_number2 = re.compile(r'((\w[A-Z])+)')
    re_number3 = re.compile(r'((\d)+)')
    mo1 = re_number1.search(password)
    mo2 = re_number2.search(password)
    mo3 = re_number3.search(password)
    if mo1 is None or mo2 is None or mo3 is None:
        return False
    else:
        return True


def check_password(password):
    if len(password) < 8:
        return False
    else:
        return check_strong(password)


password = input("Password:  ")
print(check_password(password))
