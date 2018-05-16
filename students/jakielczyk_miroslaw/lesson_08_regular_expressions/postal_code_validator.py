import re

postal_code_validator = re.compile(r'\d{2}-\d{3}')
postal_code_match = postal_code_validator.search('My postal code is64-100Leszno.')

if postal_code_match is not None:
    print('Postal code found: ' + postal_code_match.group())
else:
    print("Postal code not found")
