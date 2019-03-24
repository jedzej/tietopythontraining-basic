import pytest
import re


def email_validator(email):
    s = r'(\w+)(\.)*(\w+)*(\w[@])(\w+)(\.)(\w{2,3})'
    re_mail = re.compile(s)
    mo = re_mail.search(email)
    if mo is not None:
        if mo.group() == email:
            print(mo.group())
            return True
    else:
        return False


class TestEmailAddressValidator:
    @pytest.mark.parametrize("correct_address", [
        'aaa@aaa.pl',
        'a-a-a@aaa.pl',
        'a12a@12a.com',
    ])
    def test_valid_email_address(self, correct_address):
        assert email_validator(correct_address) is True

    @pytest.mark.parametrize("incorrect_address", [
        'aaa@a@aa.pl',
        'aaa@@aa.pl',
        'a12a.com',
    ])
    @pytest.mark.xfail
    def test_incorrect_email_address(self, incorrect_address):
        assert email_validator(incorrect_address) is False


if __name__ == '__main__':
    pytest.main()
