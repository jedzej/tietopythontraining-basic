import re


def check_phone_number(phone):
    if re.compile(r'^\d{3}-\d{3}-\d{3}$').match(phone):
        return True
    return False


def main():
    phone_num = '123-123-456'
    print('Phone number: ' + phone_num)
    print('Result: ' + str(check_phone_number(phone_num)))


if __name__ == '__main__':
    main()
