import pytest
from strong_password_detection import password_check


# ********* tests for strong password *********
@pytest.mark.parametrize("args", [
    'ksl66akijRRRs4sss',
    'jhjk&***hbhkhjVHGGH67'
])
def test_valid_string_arguments(args):
    assert password_check(args) is True


# ********* tests for weak password *********
@pytest.mark.parametrize("args", [
    'kslakji',
    'kslakijisssss',
    'kslakijissWWs',
    'kslakijisss4sss',
    'kslakijissssHHHss'
])
def test_invalid_string_arguments(args):
    assert password_check(args) is False
