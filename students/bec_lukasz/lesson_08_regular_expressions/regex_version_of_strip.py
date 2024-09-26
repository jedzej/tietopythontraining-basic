import re

strip_regex = re.compile(r'(\s*)(\w+)(\s*)')


def regex_strip(word, second=None):
    matcher = strip_regex.search(word)
    letters = []

    if second is None:
        if matcher.group(1):
            return word.replace(matcher.group(1), '')
        if matcher.group(3):
            return word.replace((matcher.group(3)), '')

    else:
        for i in second:
            letters += [i]
        second_arg_regex = re.compile(r'[' + ''.join(letters) + r']+')
        return second_arg_regex.sub('', word)


print(regex_strip(' abcdef '))
print(regex_strip(' abcdef ', 'af'))
