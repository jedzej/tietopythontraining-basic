import re


def postal_code(postal_code):
    regex = re.compile('^\d{2}(-\d{3})?$')
    return regex.match(postal_code) is not None


def main():
    test = "00-007"
    print(test, "is valid postal code: ", postal_code(test))


if __name__ == '__main__':
    main()
