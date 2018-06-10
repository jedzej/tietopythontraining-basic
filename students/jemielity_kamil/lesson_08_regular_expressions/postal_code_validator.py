import re
import pytest


class TestPostalCodeValidator:
    @pytest.mark.parametrize("code", [
        '71-111',
        '1-1',
        '111-1',
        'string',
        '12-132',
        'bla11bla71-111'
    ])
    def test_valid_post_code(self, code):
        assert postal_code_validator(code)


def postal_code_validator(code):
    regex = re.compile(r'\d{2}-\d{3}')
    mo = regex.match(code)

    if mo is not None:
        print('Postal code correct: ' + mo.group())
        return True
    else:
        print('Wrong postal code')
        return False
