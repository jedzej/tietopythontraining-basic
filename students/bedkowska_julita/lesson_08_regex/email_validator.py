import re


def check_email(email):
    if re.compile(r'^[a-zA-z0-9+._-]+[@][a-zA-Z0-9-]+[.][a-z]+$').match(email):
        return True
    return False


def main():
    email = 'julita@test.pl'
    print('Email: ' + email)
    print('Result: ' + str(check_email(email)))


if __name__ == '__main__':
    main()
