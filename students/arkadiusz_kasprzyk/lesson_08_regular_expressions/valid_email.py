#! valid_email.py
"""
https://isemail.info/about
https://tools.ietf.org/html/rfc5321
so it's virtually impossible to do it properly...
only simplest rules checked
"""

import re


def valid_email(email):
    """
    Examples
    --------
    valid_email('ab.cd@c.d')
    """

    if not re.match(r'.{5,254}', email):
        raise ValueError('e-mail address cannot exceed 254 characters and cannot be shorter then 5.')

    regex = re.compile(r'^(\w+[.-])*(\w+)@(\w+[.-])*(\w+)\.(\w+)$', re.IGNORECASE)

    if not regex.match(email):
        raise ValueError('We do not accept e-mails of this form, sorry! :(')

    return True
