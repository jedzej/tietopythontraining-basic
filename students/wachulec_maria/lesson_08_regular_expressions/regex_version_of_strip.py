import re


def regex_version_of_strip(sentence, arg=None):
    if arg is None:
        result_regex = re.compile('(\\S.*)')
        return ''.join(result_regex.findall(sentence))
    else:
        result_regex = re.compile(arg)
        return result_regex.sub('', sentence)


text = " The end of\nworld"
print(regex_version_of_strip(text, 'e'))
