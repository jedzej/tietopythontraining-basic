import re


def email_validator(text):
    email_regex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+'
                             r'(\.[a-zA-Z]{2,4}))')
    try:
        if text == email_regex.search(text).group(0):
            return 'Valid email'
    except AttributeError:
        return 'Invalid email'


email = 'sample_email@email.com'
print(email_validator(email))
