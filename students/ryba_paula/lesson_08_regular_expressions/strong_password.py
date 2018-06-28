import re


def password_check(password):
    if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(.{8,})', password):
        return True
    return False


def main():
    passwords = ("PaulaRyba1", "paula", "paulaRyba1", "PaUl1", "paulaR",
                 "PaulaRyba123", "paularyba1")

    for password in passwords:
        if password_check(password):
            print(password + " is OK")


if __name__ == '__main__':
    main()
