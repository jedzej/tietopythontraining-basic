"""
Verify the password is strong
rules:
    min 8 characters length,
    min 1 digits,
    uppercase letter,
    lowercase letter)
"""
import re


def password_check(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    password_ok = not (length_error
                       or digit_error
                       or uppercase_error
                       or lowercase_error)
    password_status = {'Password is strong.': password_ok,
                       'length to short': length_error,
                       'missing digits': digit_error,
                       'missing uppercase': uppercase_error,
                       'missing lowercase': lowercase_error}
    result = [k for k, v in password_status.items() if v is True]
    print(', '.join(result))
    return password_ok


password = input('Put password:')
password_check(password)

"""
#----------tests----------
password = 'kslakji'
print('\nPassword: ', password)
password_check(password)
password = 'kslakijisssss'
print('\nPassword: ', password)
password_check(password)
password = 'kslakijissWWs'
print('\nPassword: ', password)
password_check(password)
password = 'kslakijisss4sss'
print('\nPassword: ', password)
password_check(password)
password = 'kslakijissssHHHss'
print('\nPassword: ', password)
password_check(password)
password = 'ksl66akijRRRs4sss'
print('\nPassword: ', password)
password_check(password)
password = 'jhjk&***hbhkhjVHGGH67'
print('\nPassword: ', password)
password_check(password)
"""
