import re


def validate_email_address(address):
    regex = re.compile(r'[a-zA-Z0-9!#$%&\'*+-/=?^_`{|}~]{,64}'
                       '@[a-zA-Z0-9.-]+(\.?[a-zA-Z]{2,4})')
    if regex.match(address):
        return re.search(r'\.\.', address) is None
    return False


def main():
    addresses = [  # Valid
                 'simple@example.com',
                 'very.common@example.com',
                 'disposable.style.email.with+symbol@example.com',
                 'other.email-with-dash@example.com',
                 'fully-qualified-domain@example.com',
                 'user.name+tag+sorting@example.com',
                 'x@example.com',
                 'example-indeed@strange-example.com',
                 'admin@mailserver1',
                 '#!$%&\'*+-/=?^_`{}|~@example.org',
                 'example@s.solutions',
                 'user@localserver',
                   # Invalid
                 'Abc.example.com',
                 'A@b@c@example.com',
                 'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
                 'just"not"right@example.com',
                 'this is"not\allowed@example.com',
                 'this\ still\"not\\allowed@example.com',
                 'john..doe@example.com',
                 'john.doe@example..com',
                 '" "@example.org']

    for address in addresses:
        print(address + " - ", end="")
        if validate_email_address(address):
            print("Valid!")
        else:
            print("Invalid!")


if __name__ == "__main__":
    main()
