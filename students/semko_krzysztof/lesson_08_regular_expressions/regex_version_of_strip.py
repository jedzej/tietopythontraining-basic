"""
Write a function that takes a string and does the same
thing as the strip() string method. If no other arguments
are passed other than the string to strip, then whitespace
characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in
the second argument to the function will be removed
from the string.
"""
import re


def strip_regex(line, strip=''):
    stripped_line = re.compile(r"^ +| +$")
    result = stripped_line.sub('', line)
    if strip != '':
        arg_strip = re.compile(strip)
        result = arg_strip.sub('', result)

    return result


def main():
    print("Please input line to strip:")
    line = input()
    print("Please input optional parameter")
    arg = input()

    print(strip_regex(line, arg))


if __name__ == '__main__':
    main()
