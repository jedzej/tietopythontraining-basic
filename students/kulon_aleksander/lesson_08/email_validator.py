import re


def email_validate(email):
    regex = re.compile(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)'
                       '*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
    return regex.match(email) is not None


def main():
    text = "dupa@jasiu.com"
    print(text, "is valid email: ", email_validate(text))


if __name__ == '__main__':
    main()
