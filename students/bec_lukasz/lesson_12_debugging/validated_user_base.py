import re

# Validated user base - write script that takes email,
# password, phone number and postal code, validates
# these fields and if validation passes, saves it to
# a file as CSV with email considered as unique field.
# If a record with the same email is already in the file,
# the old record should be altered by new one. Use
# validators implemented in lesson 8, exercises 2, 3, 4 and 5.
# As part of this exercise write combined_validator function
# that takes email, password, phone number and postal code
# and throws exceptions if any of arguments
# doesn't pass validation. Add 'verbose output'.


user_data_file = 'C:\\Pajton\\user_base.csv'
user_data = []
file_content = []


def validate_email(address):
    email_check = re.compile(r'(\w+)(@)(\w+)(\.{1})(\w+)')
    me = email_check.search(address)
    try:
        me.group()
        return 0
    except AttributeError:
        return 1


def validate_strong_password(word):
    small_letter = re.compile(r'[a-z]+')
    capital_letter = re.compile(r'[A-Z]+')
    number = re.compile(r'[1-9]+')
    length_check = re.compile(r'\w{8,}')
    matchers = [small_letter.search(word), capital_letter.search(word),
                number.search(word), length_check.search(word)]
    matchers_check = []
    try:
        for i in matchers:
            if i.group():
                matchers_check += ['OK']
        if len(matchers_check) == 4:
            return 0
    except AttributeError:
        return 1


def validate_phone_number(number):
    regex = re.compile('^(\d{2,3})?(\s|-)?'
                       '(\d{3})+(\s|-)?'
                       '(\d{3})+(\s|-)?'
                       '(\d{3})+')

    matcher = regex.search(number)
    try:
        matcher.group()
        return 0

    except AttributeError:
        return 1


def validate_code(code):
    code_regex = re.compile(r'[0-9]{2}-[0-9]{3}')
    match_code = code_regex.search(code)
    try:
        match_code.group()
        return 0
    except AttributeError:
        return 1


def take_from_user():
    email = input('Enter an email ')
    password = input('Enter password: eight characters long, '
                     'contains both uppercase and lowercase '
                     'characters, and has at least one digit ')
    phone_number = input('Enter phone number ')
    postal_code = input('Enter postal code ')
    user_data.append(email)
    user_data.append(password)
    user_data.append(phone_number)
    user_data.append(postal_code)


def validate_all_data():
    email_validation = validate_email(user_data[0])
    password_validation = validate_strong_password(user_data[1])
    phone_validation = validate_phone_number(user_data[2])
    postal_code_validation = validate_code(user_data[3])
    return email_validation, password_validation, \
        phone_validation, postal_code_validation


def is_all_data_valid(verify_list):
    for i in verify_list:
        if i > 0:
            return False
        else:
            return True


def read_file_data():
    input_file = open(user_data_file, 'r')
    contents = input_file.readlines()
    input_file.close()
    for line in contents:
        file_content.append(line)


def check_if_mail_exists(email):
    input_file = open(user_data_file, 'r')
    contents = input_file.read()
    input_file.close()
    for line in contents.split():
        if email in line.split(' '):
            return True


def write_to_file(data_list):
    if is_all_data_valid(validate_all_data()):
        if check_if_mail_exists(data_list[0]):
            update_csv_file(file_content, data_list[0])
        else:
            save_to_csv(data_list[0], data_list[1],
                        data_list[2], data_list[3])


def save_to_csv(email, password, phone, code):
    data_file = open(user_data_file, 'a')
    data_file.write(email + ' ' + password +
                    ' ' + phone + ' ' + code + '\n')
    data_file.close()


def update_csv_file(new_content, email):
    data_string = user_data[0] + ' ' + \
        user_data[1] + ' ' + user_data[2]\
        + ' ' + user_data[3]
    data_file = open(user_data_file, 'w')
    for line in new_content:
        if email in line:
            line = data_string
        data_file.write(line)
    data_file.write('\n')
    data_file.close()


def main():
    take_from_user()
    validate_all_data()
    read_file_data()
    write_to_file(user_data)


if __name__ == '__main__':
    main()
