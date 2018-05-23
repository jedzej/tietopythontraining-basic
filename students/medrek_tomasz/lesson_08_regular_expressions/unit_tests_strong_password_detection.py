import pytest
from strong_password_detection import strong_password_detection


@pytest.mark.parametrize("test_input, expected", [
    ("abcdefgh", False),
    ("Abcdefgh", False),
    ("1bcdefgh", False),
    ("1Bcdefgh", True),
    ("1Bcdefghi", True),
    ("1Bcdefg", False),
    ("Abcdefg8", True),
])
def test_eval(test_input, expected):
    assert strong_password_detection(test_input) == expected
