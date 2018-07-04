import pytest
from phone_number_validator import check_phone_number


# ********* tests for valid phone number *********
@pytest.mark.parametrize("args", [
    '+48 600 600 600',
    '+48 600-600-600',
    '0048 600 600 600',
    '0048 600-600-600',
    '(+48) 600 600 600',
    '(+48) 600-600-600',
    '(0048) 600 600 600',
    '(0048) 600-600-600',
    '(0048)600 600 600',
    '(0048)600-600-600',
    '600-600-600',
    '600 600 600',
    '+48 600600600',
    '(0048) 600600600',
    '(0048)600600600',
    '(+48)600600600',
    '0048 600600600',
    '600-600 600',
    '600 600-600'
])
def test_valid_string_arguments(args):
    assert check_phone_number(args) is True


# ********* tests for invalid phone number *********
@pytest.mark.parametrize("args", [
    '+48600 600 600',
    '0048600 600 600',
    '(+48) 600-600-600-700',
    '600 600',
    '+482 600 600 600',
    '(48) 600 600 600'
])
def test_invalid_string_arguments(args):
    assert check_phone_number(args) is False
