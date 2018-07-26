import re


def is_email_valid(email):
    r = re.compile(r'[a-zA-Z_0-9.]{2,}'
                   r'@'
                   r'([a-zA-Z0-9]{2,}'
                   r'\.[a-zA-Z]{2,})'
                   r'(\.?[a-z]{2,})?')
    if r.search(email) is None:
        return False
    return True


my_email = 'adam.wulw@tieto.com'

if is_email_valid(my_email):
    print('Email OK')
else:
    print('Email format is not valid\n')
