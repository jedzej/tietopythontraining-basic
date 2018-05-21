import re


def regex_strip(text, strip=''):
    reg = re.compile(r"^ +| +$")
    result = reg.sub('', text)

    if strip != '':
        result = re.compile(strip).sub('', result)

    return result


def main():
    print(regex_strip("  strip spaces  "))
    print(regex_strip("check if that works by removing i", "i"))


if __name__ == '__main__':
    main()
