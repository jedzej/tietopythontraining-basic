import re


def email_validator(email):
    s = r'(\w+)(\.)*(\w+)*(\w[@])(\w+)(\.)(\w{2,3})'
    re_mail = re.compile(s)
    mo = re_mail.search(email)
    if mo is not None:
        if mo.group() == email:
            print(mo.group())
            return True
    else:
        return False


test = input("Email:  ")
print(email_validator(test))
