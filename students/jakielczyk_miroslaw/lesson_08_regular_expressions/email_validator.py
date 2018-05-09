import re

email_address = input("Enter email address: ")

email_regex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+      # username
                @                      # @ symbol
                [a-zA-Z0-9.-]+         # domain name
                (\.[a-zA-Z]{2,3})      # dot-something
                )''', re.VERBOSE)

email_match = email_regex.search(email_address)

if email_match is not None:
    print("given email address is correct")
else:
    print("Given email address is incorrect")
