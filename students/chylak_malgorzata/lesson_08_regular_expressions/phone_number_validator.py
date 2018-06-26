import re


def main():
    phone_number = input("Insert a phone number: ")
    if correct(phone_number):
        print("Correct!")
    else:
        print("Incorrect phone number ;(")


def correct(phone_number):
    regex = re.compile(r'(\d{2}[- ]?)?((\d{3})[- ]?(\d{3})[- ]?(\d{3}))')
    return regex.match(phone_number)


if __name__ == "__main__":
    main()
