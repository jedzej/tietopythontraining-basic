#! python3
import re
import pytest


def validate_email_address(address):
    """
    Supports most of the rules listed in:
    https://en.wikipedia.org/wiki/Email_address
    """
    regex = re.compile(r'[a-zA-Z0-9!#$%&\'*+-/=?^_`{|}~]{,64}'
                       '@[a-zA-Z0-9.-]+(\.?[a-zA-Z]{2,4})')
    if regex.match(address):
        # use negative lookaround to look for double dots
        return re.search(r'\.\.', address) is None
    return False


class TestEmailAddressValidator:
    @pytest.mark.parametrize("address", [
        'simple@example.com',
        'very.common@example.com',
        'disposable.style.email.with+symbol@example.com',
        'other.email-with-dash@example.com',
        'fully-qualified-domain@example.com',
        'user.name+tag+sorting@example.com',
        'x@example.com',
        #  '"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"
        #  @strange.example.com',
        'example-indeed@strange-example.com',
        'admin@mailserver1',
        '#!$%&\'*+-/=?^_`{}|~@example.org',
        #  '"()<>[]:,;@\\\"!#$%&\'-/=?^_`{}| ~.a"@example.org',
        'example@s.solutions',
        'user@localserver',
    ])
    def test_valid_email_address(self, address):
        assert validate_email_address(address)

    @pytest.mark.parametrize("address", [
        'Abc.example.com',  # no @ character
        'A@b@c@example.com',  # only one @ is allowed outside quotation marks
        'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
        'just"not"right@example.com',
        'this is"not\allowed@example.com',
        'this\ still\"not\\allowed@example.com',
        '1234567890123456789012345678901234567890123456789012345678901234+x'
        '@example.com',  # too long
        'john..doe@example.com',  # double dot before @
        'john.doe@example..com',  # double dot after @
        '" "@example.org',  # space between the quotes
    ])
    def test_invalid_email_address(self, address):
        assert not validate_email_address(address)
