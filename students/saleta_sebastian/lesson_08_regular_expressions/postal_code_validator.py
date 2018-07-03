import re


def check_postal_code(postal_code):
    postal_code_regex = re.compile(r'^(\d{2}[- ]\d{3})$')
    if not postal_code_regex.match(postal_code):
        return False
    return True


def main():
    sample_postal_code = '42-200'
    print(check_postal_code(sample_postal_code))


if __name__ == '__main__':
    main()
