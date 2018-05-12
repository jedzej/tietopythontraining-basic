import re


def main():
    passwd = input("Please provide password!: ")

    while not is_strong_password(passwd):
        print("Passord is too weak!")
        passwd = input("Please provide password!: ")
    print("Password accepted!")


def is_strong_password(passwd):
    has_at_least_eight = re.compile(r'.{8}')
    has_upper_case = re.compile(r'[A-Z]')
    has_lower_case = re.compile(r'[a-z]')
    has_digit = re.compile(r'\d')

    if not has_at_least_eight.search(passwd):
        print("Password is too short!")
        return False
    elif not has_upper_case.search(passwd):
        print("Password needs upper case letter!")
        return False
    elif not has_lower_case.search(passwd):
        print("Password needs lower case letter!")
        return False
    elif not has_digit.search(passwd):
        print("Password needs digit!")
        return False
    return True


if __name__ == '__main__':
    main()
