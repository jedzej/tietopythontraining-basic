"""
Postal code validator - postal code validator that checks if supplied
correct postal code: 25-894
"""
import re


def check_postal_code(postal_code):
    post_code_regex = re.compile(r'(\d{2})-(\d{3}$)')
    post_code_result = post_code_regex.match(postal_code)
    if post_code_result is not None:
        print("Postal code is valid.")
        return True
    else:
        print("Postal code isn't valid.")
        return False


post_code = input('Put postcode: ')
check_postal_code(post_code)

"""
#----------tests----------
post_code = '25-894'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '255-894'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25-8943'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '2-4'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25894'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = 'as-894'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25-sss'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25-89-255'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25-895-255'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
post_code = '25*895'
print('\nPostal Code: ', post_code)
check_postal_code(post_code)
"""
