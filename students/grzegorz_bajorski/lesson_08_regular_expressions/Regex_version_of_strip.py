import re


def my_strip(string, chars=''):
    if not chars:
        regex = re.compile(r'^\s+|\s+$')
    else:
        regex = re.compile(r'^[{0}]*|[{0}]*$'.format(chars))
    return regex.sub('', string)


print("Enter string")
string = input(str())

print("Enter strip world")
strip = input(str())

print(my_strip(string, strip))
