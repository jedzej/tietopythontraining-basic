import re


def check_if_password_is_strong(passwd):
    min_8_characters = re.compile(r'.{8}')
    upper_case = re.compile(r'[A-Z]')
    lower_case = re.compile(r'[a-z]')
    have_digit = re.compile(r'\d')

    if not min_8_characters.search(passwd):
        print('Password is less than 8 characters')
        return False
    if not upper_case.search(passwd):
        print('No upper case letters')
        return False
    if not lower_case.search(passwd):
        print('No lower case letters')
        return False
    if not have_digit.search(passwd):
        print('No digits in password')
        return False
    print('password is GIT')
    return True


def main():
    user_passwd = input('Please provide a strong password: ')
    check_if_password_is_strong(user_passwd)


if __name__ == '__main__':
    main()