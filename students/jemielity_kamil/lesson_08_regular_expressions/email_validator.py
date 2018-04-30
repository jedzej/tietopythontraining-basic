import re


def email_validator(string):
    regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9]{2,3}')
    mo = regex.search(string)
    if mo is not None:
        print(mo.group())
    else:
        print('Wrong email address')


email_validator('aaa@aaa.pl')
email_validator('a-a-a@aaa.pl')
email_validator('a12a@12a.com')
email_validator('@#@@.as.com')
