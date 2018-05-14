import pytest
import re


def phone_validator(phone_number):
    s = r'(\+\d{2})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})'
    re_number = re.compile(s)
    mo = re_number.search(phone_number)
    if mo is not None:
        if mo.group() == phone_number:
            return True
        else:
            return False
    else:
        return False


class TestPhoneNumberValidator:
    @pytest.mark.parametrize("correct_number", [
        '123-456-789',
        '198765432',
        '123 321 123',
    ])
    def test_valid_email_address(self, correct_number):
        assert phone_validator(correct_number) is True

    @pytest.mark.parametrize("incorrect_number", [
        'aaa@a@aa.pl',
        '12344',
        '123456-666666',
    ])
    @pytest.mark.xfail
    def test_incorrect_phone_number(self, incorrect_number):
        assert phone_validator(incorrect_number) is False


if __name__ == '__main__':
    pytest.main()
