import re


def check_single_regex(text, pattern):
    regex = re.compile(pattern)
    return re.findall(regex, text)


def strong_password_detection(text):
    amount_list = [len(check_single_regex(text, i)) for i in
                   ['[a-z]', '[A-Z]', '\d']]
    if len(text) < 8:
        return 'Too short'
    elif not all(amount_list):
        return "Password should contain at least one digit, uppercase" \
               " and lowercase characters"
    else:
        return "Password is strong"


password = 'MegaStrong3'
print(strong_password_detection(password))
