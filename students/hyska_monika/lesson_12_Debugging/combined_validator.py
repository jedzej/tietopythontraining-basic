import validators
import csv_functions
import logging_set


def combined_validator():
    logging_set.create_logsfile('validators_logs.log')
    # ... set email ...
    email = input('Put email:')
    while validators.check_email(email) is False:
        email = input('Put email:')
    # ... set password ...
    password = input('Put password:')
    while validators.password_check(password) is False:
        password = input('Put password:')
    # ... set postcode ...
    post_code = input('Put postcode: ')
    while validators.check_postal_code(post_code) is False:
        post_code = input('Put postcode: ')
    # ... set phone number ...
    phone_nbr = input('Put phone number: ')
    while validators.check_phone_number(phone_nbr) is False:
        phone_nbr = input('Put phone number: ')
    # save data to csv
    columns_names = ['Email', 'Password', 'Postcode', 'PhoneNumber']
    data = [email, password, post_code, phone_nbr]
    csv_functions.save_data_to_csv("emails_data.csv", columns_names,data)


def main():
    combined_validator()


if __name__ == '__main__':
    main()
