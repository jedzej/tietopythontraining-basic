#! python3
import re
import pytest

"""
Phone number validator accepts phone numbers in not separated,
space-separated or hypen-separated 9-digit format with optional country prefix
"""


def validate_phone_number(phone_number):
    regex = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    return regex.match(phone_number) is not None


class TestPhoneNumberValidator:
    @pytest.mark.parametrize("phone_number", [
        '876543210',
        '876 543 210',
        '876-543-210',
        '+48 876543210',
        '+48876543210',
        '+488 876 543 210',
        '+4 876-543-210',
    ])
    def test_valid_phone_number(self, phone_number):
        assert validate_phone_number(phone_number)

    @pytest.mark.parametrize("phone_number", [
        '76543210',
        '+ 876543210',
        '+876543210',
        ' 876543210',
        '876543210 ',
        '8X6543210'
        '123-456'
        '876-543- 210',
        '+1111 12345678',
        '876 543  210',
        'abc 543 210',
    ])
    def test_invalid_phone_number(self, phone_number):
        assert not validate_phone_number(phone_number)
