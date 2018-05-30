import re


def strip_mm(str, replacement=''):
    if not replacement:
        rgx_strip = re.compile(r'\s*(\d*\w*)\s*')
        matched = rgx_strip.search(str)
        return matched.group(1)
    else:
        regex = re.compile(r'^[{0}]*|[{0}]*$'.format(replacement))
        return regex.sub("", str)


if __name__ == '__main__':
    str = input("Enter yout text: ")
    print(strip_mm(str, replacement='t'))
