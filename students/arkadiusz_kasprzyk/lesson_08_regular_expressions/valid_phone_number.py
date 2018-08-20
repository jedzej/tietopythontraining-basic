# valid_phone_number.py

import re

def valid_phone_number(phone):
    """
    Examples
    --------
    valid_phone_number('123-456-789')
    valid_phone_number('+48 123-456-789')
    valid_phone_number('0048 123-456-789')
    valid_phone_number('123 456 789')
    valid_phone_number('+48 123 456 789')
    valid_phone_number('+48 123-456 789')   # OK, but should it be OK?

    valid_phone_number('+48 123 456')       # ValueError
    valid_phone_number('23 456 789')        # ValueError
    valid_phone_number('3 456 789')         # ValueError
    valid_phone_number('0123 456 789')      # ValueError
    """
    regex = re.compile(r'^((\+|00)\d{2} )?(\d{3}[- ]){2}(\d{3})$')
    if not regex.match(phone):
        raise ValueError("This is not valid phone number.")
    else:
        return True
