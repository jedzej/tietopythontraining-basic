import pytest
from phone_number_validator import phone_number_validator


@pytest.mark.parametrize("test_input, expected", [
    (r'696 403 895', True),
    (r'696-403-895', True),
    (r'696403895', True),
    (r'696-403 895', True),
    (r'-696-403-895', False),
    (r'+++-696-403-895', False),
    (r'+48 696 403 895', True),
    (r'+48-696-403-895', True),
    (r'+48696403895', True),
    (r'+48696-403 895', True),
    (r'+48 696 403 8956', False),
    (r'+8 696 403 895', False),
    (r'+484 696 403 895', False),
    (r'+8696403895', False),
    (r'48696403895', False),
    (r'+a8 696 403 895', False),
    (r'696 403', False),
    (r'696 403 403 403', False),
])
def test_eval(test_input, expected):
    assert phone_number_validator(test_input) == expected
