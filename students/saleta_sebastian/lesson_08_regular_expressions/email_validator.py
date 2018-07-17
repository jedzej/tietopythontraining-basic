import re


def check_email(email_address):
    mail_regex = re.compile(r'^[a-zA-z0-9+._-]+[@][a-zA-Z0-9-]+[.][a-z]+$')
    if mail_regex.match(email_address):
        return True
    return False


def main():
    sample_email = 'testmail@tieto.com'
    print(check_email(sample_email))


if __name__ == '__main__':
    main()
