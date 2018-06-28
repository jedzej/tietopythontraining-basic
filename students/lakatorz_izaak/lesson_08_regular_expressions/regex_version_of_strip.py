# Write a function that takes a string and does the same thing as the strip(
# ) string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second
# argument to the function will be removed from the string.


import re


def my_strip(split_str, chars=' '):
    if chars == ' ':
        word_regex = re.compile(r'(^\s+)|(\s+$)')
        print(word_regex.sub('', split_str))
    else:
        word_regex = re.compile(r'[{}]'.format(chars))
        print(word_regex.sub('', split_str))


def main():
    my_strip('   Cat name is Filemon.   ')
    my_strip('Cat name is Filemon.  ', 'Caeo')


if __name__ == "__main__":
    main()
