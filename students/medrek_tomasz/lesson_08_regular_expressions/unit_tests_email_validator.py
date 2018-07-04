import pytest
from email_validator import email_validator


@pytest.mark.parametrize("test_input, expected", [
    # Examples taken from: https://en.wikipedia.org/wiki/Email_address#Examples
    # ommitted localhost domains.
    (r"jsimple@example.com", True),
    (r"very.common@example.com", True),
    (r"disposable.style.email.with+symbol@example.com", True),
    (r"other.email-with-dash@example.com", True),
    (r"fully-qualified-domain@example.com", True),
    (r"user.name+tag+sorting@example.com", True),
    (r"x@example.com", True),
    (r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@strange.example.com',
     True),
    (r'example-indeed@strange-example.com', True),
    (r"#!$%&'*+-/=?^_`{}|~@example.org", True),
    (r'"()<>[]:,;@\\\"!#$%&-/=?^_`{}|~.a"@example.org', True),
    (r'example@s.solutions.fr', True),
    (r'Abc.example.com', False),
    (r'A@b@c@example.com', False),
    (r'a"b(c)d,e:f;g<h>i[j\k]l@example.com', False),
    (r'just"not"right@example.com', False),
    (r'this is"not\allowed@example.com', False),
    (r'this\ still\"not\\allowed@example.com', False),
    (r'1234567890123456789012345678901234567890123456789012345678901234+x@'
     'example.com', False),
    (r'john..doe@example.com', False),
    (r'john.doe@example..com', False),
    (r'" "@example.org', False),
    (r'"John..Doe"@example.com', True),
    # Own examples
    (r'"John.Doe"@example-site.com', True),
    (r'"John.Doe"@-example.com', False),
    (r'"John.Doe"@example.c', False),
    (r'"John.Doe"@-example.commm', False),
    (r'"John.Doe"@linux.simply-far-too-long-dns-label-omg-63-letters-are-a-lot'
     '-more-than-i-was-expecting.com', False),
])
def test_eval(test_input, expected):
    assert email_validator(test_input) == expected
