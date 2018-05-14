import re


def email_validator(email):

    re_mail = re.compile(r'''((\w{1,})(\.{1})*(\w{1,})*(\w[@]{1})(\w{1,})(\.{1})(\w{2,3}))''')
    mo = re_mail.search(email)

    if mo != None:
        if mo.group() == email:
            print(mo.group())
            return True
    else:
        return False


test = input("Email:  ")
print(email_validator(test))
