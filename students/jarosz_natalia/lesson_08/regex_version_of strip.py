import re


def regex_strip(string, chars_to_remove):
    strip_regex = re.compile('[%s]' % chars_to_remove)
    print(strip_regex.sub('', string))


def main():
    regex_strip(string="zaq1@WSX", chars_to_remove="zaq")


if __name__ == '__main__':
    main()
