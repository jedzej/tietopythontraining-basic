import pytest
from postal_code_validator import check_postal_code


# ********* tests for valid phone number *********
@pytest.mark.parametrize("args", [
    '25-894',
    '00-000'
])
def test_valid_string_arguments(args):
    assert check_postal_code(args) is True


# ********* tests for invalid phone number *********
@pytest.mark.parametrize("args", [
    '255-894',
    '25-8943',
    '2-4',
    '25894',
    'as-894',
    '25-sss',
    '25-89-255',
    '25-895-255',
    '25*895'
])
def test_invalid_string_arguments(args):
    assert check_postal_code(args) is False
