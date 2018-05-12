import re


def phone_number_validator(number):
    r_number = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    if r_number.match(number):
        return 1


def main():
    set_of_phone_numbers = ("text",
                            "email@email.com",
                            "12/345",
                            "59-430",
                            "1",
                            "12",
                            "123",
                            "1234",
                            "12345",
                            "123456",
                            "1234567",
                            "12345678",
                            "123456789",
                            "123 456 789",
                            "123-456-789",
                            "+48123456789",
                            "+48 123 456 789",
                            "+48-123-456-789",
                            "+a123456789",
                            "+ab123456789",
                            "+ab 123 456 789",
                            "+ab-123-456-789")

    for number in set_of_phone_numbers:
        if phone_number_validator(number):
            print(number + " is phone number")


if __name__ == "__main__":
    main()
