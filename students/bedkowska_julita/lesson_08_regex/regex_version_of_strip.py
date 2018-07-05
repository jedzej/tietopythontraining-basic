import re


def regex_strip(text, chars=''):
    escape_chars = re.escape(chars)
    regex = re.compile(r'^[' + escape_chars + ']*(.*?)[' + escape_chars + ']*$')
    match = regex.search(text)
    return match.group(1)


def main():
    text = 'aabtaererewwcb'
    characters = 'abc'
    print('Text: ' + text)
    print('Characters: ' + characters)
    print('Result: ' + regex_strip(text, characters))


if __name__ == '__main__':
    main()
