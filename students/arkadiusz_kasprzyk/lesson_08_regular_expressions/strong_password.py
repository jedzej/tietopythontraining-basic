import re


def strong_password(password):
    """
    Examples
    --------
    strong_password('abcdefg')
    strong_password('abcdefgh')
    strong_password('ABCDEFGH')
    strong_password('Abcdefgh')
    strong_password('Abcdefg0')
    strong_password('12345678')
    """
    if not re.search(r'^.{8,}$', password):
        raise ValueError('Password must have at least 8 characters.')
    elif not re.search(r'[a-z]', password):
        raise ValueError('Password must have at least 1 lowercase letter.')
    elif not re.search(r'[A-Z]', password):
        raise ValueError('Password must have at least 1 UPPERcase letter.')
    elif not re.search(r'\d', password):
        raise ValueError('Password must have at least 1 digit.')
    else:
        return True
