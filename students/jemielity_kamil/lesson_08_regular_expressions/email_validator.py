import re
import pytest


class TestEmailAddressValidator:
    @pytest.mark.parametrize("address", [
        'aaa@aaa.pl',
        'a-a-a@aaa.pl',
        'a12a@12a.com',
        '@#@@.as.com',
        'a'
    ])
    def test_valid_email_address(self, address):
        assert email_validator(address)


def email_validator(string):
    regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9]{2,3}')
    mo = regex.search(string)
    if mo is not None:
        print(mo.group())
        return True
    else:
        print('Wrong email address')
        return False


# email_validator('aaa@aaa.pl')
# email_validator('a-a-a@aaa.pl')
# email_validator('a12a@12a.com')
# email_validator('@#@@.as.com')
