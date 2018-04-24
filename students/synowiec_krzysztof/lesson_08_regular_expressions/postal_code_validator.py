import re


def main():
    postal_code = input("Provide postal code ex. 59-100: ")
    if is_postal_code_valid(postal_code):
        print("Valid postal code!")
    else:
        print("Invalid postal code!")


def is_postal_code_valid(postal_code):
    regex = re.compile(r'\d{2}-\d{3}')
    return regex.match(postal_code)


if __name__ == '__main__':
    main()
