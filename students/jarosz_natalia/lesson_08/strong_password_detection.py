import re


def strong_password(password):
    regex = re.compile(r'^(?=.*\d{1,8})(?=.*[a-z]{1,8})(?=.*[A-Z]{1,8'
                       r'})(?=.*\w).{8,}$')
    if regex.search(password) is not None:
        return True
    else:
        return False


def main():
    password = "Dufbdfbkdsb1236##"
    if strong_password(password):
        print("Password is strong :)")
    else:
        print("Password is too weak :/")


if __name__ == "__main__":
    main()
