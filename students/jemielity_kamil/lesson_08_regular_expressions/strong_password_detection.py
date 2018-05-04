import re


def strong_password_detection(password):
    regex = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?\W).{8,}')
    mo = regex.search(password)

    if mo is not None:
        print('Correct password')
    else:
        print('Incorrect password')


strong_password_detection('123456Az@')
strong_password_detection('R1ssdf#x')
strong_password_detection('111')
strong_password_detection('R@z1')
strong_password_detection('12-132AAa')
