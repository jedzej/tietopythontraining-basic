import re
import pytest


class TestPassword:
    @pytest.mark.parametrize("password", [
        '123456Az@',
        'R1ssdf#x',
        '111',
        'R@z1',
        '12-132AAa'
    ])
    def test_password(self, password):
        assert strong_password_detection(password)


def strong_password_detection(password):
    regex = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?\W).{8,}')
    mo = regex.search(password)

    if mo is not None:
        print('Correct password')
        return True
    else:
        print('Incorrect password')
        return False
