#! python3
import re
import pytest


def validate_postal_code_pl(postal_code):
    regex = re.compile(r'^\d{2}-\d{3}$')
    return regex.match(postal_code) is not None


class TestPostalCodeValidator:
    def test_valid_postal_code(self):
        assert validate_postal_code_pl('98-200')

    @pytest.mark.parametrize("postal_code", [
        '12345',
        '1-234',
        '12-3',
        '12-3456',
        '123-456',
        '12x-345'
    ])
    def test_invalid_postal_code(self, postal_code):
        assert not validate_postal_code_pl(postal_code)
