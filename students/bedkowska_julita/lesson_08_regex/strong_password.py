import re


def check_password(password):
    if not re.compile(r'.{8}').search(password):
        print('Password is less than 8 characters')
        return False
    if not re.compile(r'[A-Z]').search(password):
        print('No upper case letters')
        return False
    if not re.compile(r'[a-z]').search(password):
        print('No lower case letters')
        return False
    if not re.compile(r'\d').search(password):
        print('No digits in password')
        return False
    print('Password is strong')
    return True


def main():
    test_pass = "ABC123asdasdas"
    print('Password: '+test_pass)
    check_password(test_pass)


if __name__ == '__main__':
    main()
