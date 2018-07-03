import re


def strong_password(word):

    small_letter = re.compile(r'[a-z]+')
    capital_letter = re.compile(r'[A-Z]+')
    number = re.compile(r'[1-9]+')
    length_check = re.compile(r'\w{8,}')

    matchers = [small_letter.search(word), capital_letter.search(word),
                number.search(word), length_check.search(word)]
    matchers_check = []

    try:
        for i in matchers:
            if i.group():
                matchers_check += ['OK']

        if len(matchers_check) == 4:
            return 'Password is strong: ' + word

    except AttributeError:
        return 'Password do not match requirements: ' + word


print(strong_password('ab1Zasda'))
print(strong_password('ab1Zas'))
print(strong_password('ab1asdaz'))
print(strong_password('AZXCASD2'))
