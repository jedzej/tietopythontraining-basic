#! python3
import re
import pytest

"""
Strong password requirements:
- at least 8 characters long
- contains both uppercase and lowercase characters
- has at least one digit
"""


def check_password_strength(password):
    regex = re.compile(r'.{8,}')
    if regex.search(password) is None:
        print("The password should be at least 8 characters long")
        return False

    # Positive lookahead
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')
    if regex.search(password) is None:
        print("The password should contains both uppercase and lowercase "
              "characters and has at least one digit")
        return False
    return True


class TestPasswordStrengthCheck:
    @pytest.mark.parametrize("password", [
        'MyPython12',
        '    MyPython12   ',
        'Mypython12',
        'myPython12',
        'My1python',
    ])
    def test_valid_password_strength(self, password):
        assert check_password_strength(password)

    @pytest.mark.parametrize("password", [
        'Python1',
        'mypython12',
        'MYPYTHON12',
        'Mypython',
    ])
    def test_invalid_password_strength(self, password):
        assert not check_password_strength(password)
