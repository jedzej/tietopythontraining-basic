"""
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument
and returns a string with all the items separated by
a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
"""


def coma_separate_string(l):
    if not isinstance(l, list):
        raise ValueError("Expected list argument")
    result = ""
    for i in range(len(l) - 1):
        result += str(l[i]) + ", "
    result += "and " + l[len(l) - 1]
    return result


def coma_separet_string_without_last_coma(l):
    if not isinstance(l, list):
        raise ValueError
    result = ''
    result = ', '.join(l[:-1])
    result += ' and ' + l[-1]
    return result


if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(coma_separate_string(spam))
    print(coma_separet_string_without_last_coma(spam))
