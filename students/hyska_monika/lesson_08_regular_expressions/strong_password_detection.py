"""
Verify the password is strong
rules:
    min 8 characters length,
    min 1 digits,
    uppercase letter,
    lowercase letter)
- tests: strong_password_detection_pytest.py
"""
import re


def password_check(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    password_ok = not (length_error or digit_error or
                       uppercase_error or lowercase_error)
    password_status = {'Password is strong.': password_ok,
                       'length to short': length_error,
                       'missing digits': digit_error,
                       'missing uppercase': uppercase_error,
                       'missing lowercase': lowercase_error}
    result = [k for k, v in password_status.items() if v is True]
    print(', '.join(result))
    if password_ok is True:
        return True
    else:
        return False


def main():
    password = input('Put password:')
    password_check(password)


if __name__ == '__main__':
    main()
