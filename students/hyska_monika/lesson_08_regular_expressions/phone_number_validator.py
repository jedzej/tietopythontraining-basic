"""
 Phone number validator accepts phone numbers:
    - not separated,
    - space-separated
    - hypen-separated
    - 9-digit format
    - optional country prefix

eg. correct numbers:
+48 600 600 600
+48 600-600-600
0048 600 600 600
0048 600-600-600
(+48) 600 600 600
(+48) 600-600-600
(0048) 600 600 600
(0048) 600-600-600
(0048)600 600 600
(0048)600-600-600
600-600-600
600 600 600
+48 600600600
(0048) 600600600
(0048)600600600
(+48)600600600
0048 600600600
"""
import re


def check_phone_number(phone_number):
    phone_number_regex = re.compile(r'''(
        (((00|\+)\d{2}\s)|(\((00|\+)\d{2}\)(\s)?))?   # country code
        \d{3}                                         # first 3 digits
        ((-|\s)?\d{3}){2}$                            # two groups: space or - and 3 digits
        )''', re.VERBOSE)
    phone_number_result = phone_number_regex.match(phone_number)
    if phone_number_result is not None:
        print("Phone number is valid.")
        return True
    else:
        print("Phone number isn't valid.")
        return False


phone_nbr = input('Put phone number: ')
check_phone_number(phone_nbr)

"""
# ---------- tests ---------
# ---------- correct cases ----------
print('\ncorrect:')
phone_nbr = '+48 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '+48 600-600-600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '0048 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(+48) 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(+48) 600-600-600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048) 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048) 600-600-600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048)600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048)600-600-600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '600-600-600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '+48 600600600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048) 600600600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(0048)600600600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '0048 600600600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(+48)600600600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

# ---------- incorrect cases ----------
print('\nincorrect:')
phone_nbr = '+48600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '0048600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(+48) 600-600-600-700'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '+482 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)

phone_nbr = '(48) 600 600 600'
print('\nPhone Number: ', phone_nbr)
check_phone_number(phone_nbr)
"""
