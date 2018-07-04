import re


def main():
    postal_code = input("Insert postal code: ")
    if valid(postal_code):
        print("Correct")
    else:
        print("Invalid postal code")


def valid(postal_code):
    regex = re.compile(r'\d{2}-\d{3}')
    return regex.match(postal_code)


if __name__ == "__main__":
    main()
