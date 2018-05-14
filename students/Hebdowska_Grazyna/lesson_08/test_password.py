import pytest
import re


def check_strong(password):

    re_number1 = re.compile(r'((\w[a-z])+)')
    re_number2 = re.compile(r'((\w[A-Z])+)')
    re_number3 = re.compile(r'((\d)+)')
    mo1 = re_number1.search(password)
    mo2 = re_number2.search(password)
    mo3 = re_number3.search(password)
    if mo1 is None or mo2 is None or mo3 is None:
        return False
    else:
        return True


class TestStrongPasword:
    @pytest.mark.parametrize("correct_password", [
        '123ala7T9',
        'ajk19ZXCV432',
        'QWerty12345',
    ])
    def test_strong_password(self, correct_password):
        assert check_strong(correct_password) is True

    @pytest.mark.parametrize("incorrect_password", [
        'SDFGFSGD1222',
        '12344',
        'asdsadfdfdf',
    ])
    @pytest.mark.xfail
    def test_incorrect_password(self, incorrect_password):
        assert check_strong(incorrect_password) is False


if __name__ == '__main__':
    pytest.main()
