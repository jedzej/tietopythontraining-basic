import re


def check_password(password):
    rgx_strip = re.compile(r'[0-9]+[a-zA-Z]{8,}|[a-zA-Z]{8,}[0-9]+')
    matched = rgx_strip.search(password)
    if matched:
        print("Strong Password")
    else:
        print("Weak Password")


if __name__ == '__main__':
    password = input()
    check_password(password)
