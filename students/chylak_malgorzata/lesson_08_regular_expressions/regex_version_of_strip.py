import re


def strip_string(text, character=''):

    if character == '' or character == ' ':
        regex = re.compile(r'^[\s+]|[\s+]$')
    else:
        regex = re.compile(r'^[' + character + ']*|[' + character + ']*$')

    mo = re.sub(regex, '', text)
    return mo


print(strip_string(' Ala ma kota '))
print(strip_string('Ala ma kota', 'Alamakota'))
