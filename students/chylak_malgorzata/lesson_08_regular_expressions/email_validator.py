import re


def main():
    email_address = input("Type an email address: ")
    if valid(email_address):
        print("Correct!")
    else:
        print("Invalid email address")


def valid(email_address):
    regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9]{2,3}')
    return regex.match(email_address)


if __name__ == "__main__":
        main()
