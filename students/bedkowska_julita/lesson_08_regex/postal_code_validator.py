import re


def check_postal_code(postal_code):
    if re.compile(r'^\d{2}-\d{3}$').match(postal_code):
        return True
    return False


def main():
    postal_code = '54-123'
    print('Postal code: ' + postal_code)
    print('Result: ' + str(check_postal_code(postal_code)))


if __name__ == '__main__':
    main()
