import re


def check_strong(password):

    re_number1 = re.compile(r'''((\w[a-z]{1,})+)''')
    re_number2 = re.compile(r'''((\w[A-Z]{1,})+)''')
    re_number3 = re.compile(r'''((\d{1,})+)''')
    mo1 = re_number1.search(password)
    mo2 = re_number2.search(password)
    mo3 = re_number3.search(password)
    if mo1 == None :
        return False
    elif mo2 == None:
        return False
    elif mo3 == None:
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
