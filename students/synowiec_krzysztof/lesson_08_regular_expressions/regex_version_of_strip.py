import re


def main():
    s = "Ala ma kota"
    print(myown_strip(s))
    print(myown_strip(s, 'a'))


def myown_strip(s, r=' '):
    regex = re.compile(r'{}*'.format(r))
    return regex.sub('', s)


if __name__ == '__main__':
    main()
