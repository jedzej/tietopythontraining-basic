import re
import pytest


class TestPhoneNumber:
    @pytest.mark.parametrize("phone", [
        '666-666-666',
        '666666666',
        '48-666-666-666',
        '666 666 666',
        '48 666 666 666',
        'string',
        'raz-dwa-trzy'
    ])
    def test_valid_phone(self, phone):
        assert phone_validator(phone)


def phone_validator(number):
    regex = re.compile(r'(\d{2}[- ]?)?((\d{3})[- ]?(\d{3})[- ]?(\d{3}))')
    mo = regex.search(number)
    if mo is not None:
        print(mo.group())
        return True
    else:
        print('Wrong phone number')
        return False
