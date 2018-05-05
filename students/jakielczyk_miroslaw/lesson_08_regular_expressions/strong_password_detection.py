import re


def validate_strong_password(password):
    strong_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([\w!@#$%^&*(),.?]{8,})$')
    if strong_password.search(password) is not None:
        return True
    else:
        return False


def main():
    password = "34adbrcdfgh1234567834hTg12)(.,"
    if validate_strong_password(password):
        print("Password is strong")
    else:
        print("Password is weak")


if __name__ == "__main__":
    main()
