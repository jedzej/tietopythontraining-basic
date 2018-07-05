import re


def password_checker(password):
    regex = re.compile(r'.{8,}')
    if regex.search(password) is None:
        print("Password must be longer than 7 characters.")
        return False

    regex = re.compile(r'([a-z])')
    if regex.search(password) is None:
        print("No lowercase!")
        return False
    regex = re.compile(r'([A-Z])')
    if regex.search(password) is None:
        print("No uppercase!")
        return False
    regex = re.compile(r'([0-9])')
    if regex.search(password) is None:
        print("No digit!")
        return False

    print("The password is STRONG")
    return True


def main():
    password = "Test123#"
    password_checker(password)


if __name__ == '__main__':
    main()
