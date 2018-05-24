import re


def regex_strip(some_string, chars_to_strip):
    if re.search(r"[\.\*\\]", chars_to_strip) is not None:
        result = re.sub("^" + re.escape(chars_to_strip) + "*", '', some_string)
        result = re.sub(re.escape(chars_to_strip) + "*$", '', result)
    else:
        result = re.sub(r'^' + chars_to_strip + '*', '', some_string)
        result = re.sub(chars_to_strip + '*$', '', result)
    return result


# Prompts for user input
# print(regex_strip("...test...", "."))
# print(regex_strip("  test ", " "))
userString = input('Please enter a string value: ')
userChar = input('Please enter a character to strip from the string:')
print("Result with use of regex: " + regex_strip(userString, userChar))
print("Result2: " + userString.strip(userChar))
