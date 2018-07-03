import re


def validate_email(address):
    email_check = re.compile(r'(\w+)(@)(\w+)(\.{1})(\w+)')
    me = email_check.search(address)
    try:
        me.group()
        return 'Valid email address: ' + address
    except AttributeError:
        return 'Not valid email address' + address


print(validate_email('ed@ad.pl'))
print(validate_email('ed@adpl'))
print(validate_email('edad.pl'))
print(validate_email('ed@ad'))
