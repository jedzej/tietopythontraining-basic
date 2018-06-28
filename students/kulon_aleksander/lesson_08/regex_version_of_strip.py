import re


def regex_strip(text, char=''):
    if char == '':
        regex = re.compile(r'\S+.*\S')
        mo = regex.search(text)
        result = mo.group()
        return result
    else:
        regex = re.compile(char)
        result = regex.sub('', text)
        return result


def main():
    text = "  testraz test dwa test test cztery piec  "
    print(regex_strip(text))
    print(regex_strip(text, 'test'))


if __name__ == '__main__':
    main()
