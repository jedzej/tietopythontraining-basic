import re


def check_password_strength(password):
    regex = re.compile(r'.{8,}')
    if regex.search(password) is None:
        print("The password should be at least 8 characters long")
        return False
    
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]){8,}')
    if regex.search(password) is None:
        print("The password should contains both uppercase and lowercase "
              "characters and has at least one digit")
        return False
    return True


def main():
    set_of_passwords = ("12Kra$nal!",
                        "pass123",
                        "MySecretePassword",
                        "Password123")

    for password in set_of_passwords:
        print("\"" + password + "\" - ", end="")
        if check_password_strength(password):
            print("Strong password")


if __name__ == "__main__":
    main()
