import re


def strong_password_detection(password):
    r_password = re.compile(r'^(.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')
    if r_password.match(password):
        return 1


def main():
    set_of_r_passwords = ("Karinanartowska",
                     "karinanartowska1",
                     "Karina1",
                     "KARINANARTOWSKa1",
                     "KarinaNartowska1")
    for password in set_of_r_passwords:
        if strong_password_detection(password):
            print(password + " is strong password")


if __name__ == "__main__":
    main()
