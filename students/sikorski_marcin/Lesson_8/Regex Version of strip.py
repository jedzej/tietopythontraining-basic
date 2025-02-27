import re

string_to_check = input("Enter a string to strip: ")
characters_to_delete = input("Enter the characters you want to be striped: ")


def stripping_regex(string_to_check, characters_to_delete):
    strip_regex = re.compile('[%s]' % characters_to_delete)
    return strip_regex.sub('', string_to_check)

print(stripping_regex(string_to_check, characters_to_delete))
