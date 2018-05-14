import re

'''
write phone number validator 
that accepts phone numbers in not separated, 
space-separated or hypen-separated 
9-digit format with optional country prefix
'''


def validate_phone_number(number):
    regex = re.compile('^(\d{2,3})?(\s|-)?'
                       '(\d{3})+(\s|-)?'
                       '(\d{3})+(\s|-)?'
                       '(\d{3})+')

    matcher = regex.search(number)
    try:
        matcher.group()
        return 'Valid number: ' + number

    except AttributeError:
        return 'Not valid number: ' + number


print(validate_phone_number('123'))
print(validate_phone_number('132-123'))
print(validate_phone_number('1823-123-123'))
print(validate_phone_number('132-1234-123'))
print(validate_phone_number('1323-123-1234'))
print(validate_phone_number('1323-1232-1232'))
print()
print(validate_phone_number('123123123'))
print(validate_phone_number('123 123 123'))
print(validate_phone_number('123-123-123'))
print()
print(validate_phone_number('71 123 123 123'))
print(validate_phone_number('71-123-123-123'))
print(validate_phone_number('71123123123'))
print()
print(validate_phone_number('711-123-123-123'))
print(validate_phone_number('711 123 123 123'))
print(validate_phone_number('711123123123'))
