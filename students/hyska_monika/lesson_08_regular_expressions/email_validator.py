"""
Email validator
- email validator that checks if supplied string is valid e-mail address
correct emails:
    anaddd@gmail.com
    a@gmail.com
    432423@gmail.pl
    AnsSisfd.sf78767sa@gmail.coma
    anaddd@gmaxxxxxxxxxxil.com
"""
import re


def check_email(emial):
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-] +      # username
        @                       # @ symbol
        [a-zA-Z0-9.-] +         # domain name
        (\.[a-zA-Z]{2,4}$)       # dot and 2 - 4 letters
        )''', re.VERBOSE)
    email_result = email_regex.match(email)
    if email_result is not None:
        print("Email is valid.")
        return True
    else:
        print("Email isn't valid.")
        return False


email = input('Put email:')
check_email(email)

"""
#----------tests----------
email = 'anaddd@gmail.com'
print('\nEmail: ', email)
check_email(email)
email = 'a@gmail.com'
print('\nEmail: ', email)
check_email(email)
email = '432423@gmail.com'
print('\nEmail: ', email)
check_email(email)
email = 'AnsSisfd.sf78767sa@gmail.com'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78767sagmail.com'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78767sa@gmailcom'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78767sa@g'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78767sa@.com'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78767sa@.'
print('\nEmail: ', email)
check_email(email)
email = 'a@g'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78kk'
print('\nEmail: ', email)
check_email(email)
email = 'anisfd.sf78kk@dasmda.comcom'
print('\nEmail: ', email)
check_email(email)
email = 'sdssssssssssssssssssssss78767sa@gmaisssssssssssssssl.cssssssssssom'
print('\nEmail: ', email)
check_email(email)
email = 'anaddd@gmaxxxxxxxxxxil.com'
print('\nEmail: ', email)
check_email(email)
"""
