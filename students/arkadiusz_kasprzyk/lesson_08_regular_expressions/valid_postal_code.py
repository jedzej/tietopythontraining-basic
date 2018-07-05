# valid_postal_code.py

import re

def valid_postal_code(postal):
    """
    Examples
    --------
    valid_postal_code('12-345')
    valid_postal_code('12-34')  # ValueError
    valid_postal_code('1-345')  # ValueError
    valid_postal_code('012-345')  # ValueError
    valid_postal_code('A2-345')  # ValueError
    """
    regex = re.compile(r'^\d{2}-\d{3}')
    if not regex.match(postal):
        raise ValueError("Polish postal code is of the format DD-DDD where each D is a separate digit.")
    else:
        return True
