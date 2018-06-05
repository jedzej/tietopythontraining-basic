import re


def strip_version(string, character=''):

    if character == '' or character == ' ':
        regex = re.compile(r'^[\s+]|[\s+]$')
    else:
        regex = re.compile(r'^[' + character + ']*|[' + character + ']*$')

    mo = re.sub(regex, '', string)
    return mo


print(strip_version(' raz dwa trzy '))
print(strip_version('raz dwa trzy', 'razdzy'))
