import re
import pytest


def email_validator(some_email):
    regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    result = regex.match(some_email)
    if result is None:
        print("email is not valid")
    else:
        print("email is valid")
    return result


# user_email = input("Please enter the email address: ")
# email_validator(user_email)


class TestEmailAddressValidator:
    @pytest.mark.parametrize("correct_address", [
        'aaa@aaa.pl',
        'a-a-a@aaa.pl',
        'a12a@12a.com',
    ])
    def test_valid_email_address(self, correct_address):
        assert email_validator(correct_address) is not None

    @pytest.mark.parametrize("incorrect_address", [
        'aaa@a@aa.pl',
        'aaa@@aa.pl',
        'a12a.com',
    ])
    @pytest.mark.xfail
    def test_incorrect_email_address(self, incorrect_address):
        assert email_validator(incorrect_address) is None
