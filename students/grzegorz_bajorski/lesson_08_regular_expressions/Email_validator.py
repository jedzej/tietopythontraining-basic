import re


print("Enter email adress")
addressToVerify = input(str())
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)''*@[a-z0-9-]+'
                 '(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match is None:
    print('Bad Syntax')
else:
    print('Email is OK')
