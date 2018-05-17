import re

phone_number = input("Enter phone number: ")

phone_num_regex = re.compile(r'''(
                    ((^\+(\d){2,3})?\s\d{3}\s\d{3}\s\d{3})       # space separated
                    |((\+(\d){2,3})?\d{9})                       # no separated
                    |((\+(\d){2,3})?-?\d{3}-?\d{3}-?\d{3}$)      # hyphen-separated
                    )''', re.VERBOSE)

validate_phone_number = phone_num_regex.search(phone_number)

if validate_phone_number is not None:
    print("Given phone number is correct ", validate_phone_number.group(0))
else:
    print("Given phone number is incorrect")
