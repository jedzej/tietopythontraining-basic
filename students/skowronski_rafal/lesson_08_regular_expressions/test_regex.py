import pytest
import regex
from regex import PostalCodeKind

strip_test_data = [
    ('foo', None),
    (' foo', None),
    ('foo ', None),
    (' foo ', None),
    ('        foo ', None),
    ('        foo buz   ', None),
    (' foo', ' f'),
    (' foo', 'o'),
    ('foo buz bar', 'foobar '),
    ('   spacious   ', None),
    ('www.example.com', 'cmowz.'),
    ('#....... Section 3.2.1 Issue #32 .......', '.#! ')
]


password_test_data = [
    ('Foo12', False),
    ('foofoofoo', False),
    ('FooFooFoo', False),
    ('foo1foo2foo3', False),
    ('Foo1Foo2', True),
]


email_test_data = [
    ('example@foo.com', True),
    ('example@fo-o.com', True),
    ('example@fo@-o.com', False),
    ('example@_foo.com', False),
    ('example@-foo.com', True),
    ('example@' + 'p' * 64 + '.com', False),
    ('example@' + 'p' * 63 + '.com', True),
    ('example@' +
     'p' * 63 +
     '.' + 'p' * 63 +
     '.' + 'p' * 63 +
     '.' + 'p' * 63 +
     '.com', False),
    ('example@' +
     'p' * 63 +
     '.' + 'p' * 63 +
     '.' + 'p' * 63 +
     '.com', True),
    ('.example@foo.com', False),
    ('example.@foo.com', False),
    ('.example.@foo.com', False),
    ('exa.mp%%le@foo.com', True),
]


postal_code_test_data = [
    ('12-123', PostalCodeKind.POLISH, True),
    ('12-12a', PostalCodeKind.POLISH, False),
    ('1a-123', PostalCodeKind.POLISH, False),
    ('12123', PostalCodeKind.POLISH, False),
    ('123-123', PostalCodeKind.POLISH, False),
    ('12-1234', PostalCodeKind.POLISH, False),
    ('1-123', PostalCodeKind.POLISH, False),
    ('12-12', PostalCodeKind.POLISH, False),
    ('1234', PostalCodeKind.AMERICAN, True),
    ('123a', PostalCodeKind.AMERICAN, False),
    ('123', PostalCodeKind.AMERICAN, False),
    ('12345', PostalCodeKind.AMERICAN, False),
    ('12345-1234', PostalCodeKind.AMERICAN, True),
    ('12345-123a', PostalCodeKind.AMERICAN, False),
    ('1234a-1234', PostalCodeKind.AMERICAN, False),
    ('123456-1234', PostalCodeKind.AMERICAN, False),
    ('12345-12345', PostalCodeKind.AMERICAN, False),
    ('1234-1234', PostalCodeKind.AMERICAN, False),
    ('12345-123', PostalCodeKind.AMERICAN, False),
]


mobile_phone_test_data = [
    ('123456789', True),
    ('+48 123456789', True),
    ('123-456-789', True),
    ('+48 123-456-789', True),
    ('123 456 789', True),
    ('+48 123 456 789', True),
    ('0048 123 456 789', True),
    ('00481 123 456 789', False),
    ('00b 123 456 789', False),
    ('12a 456 789', False),
    ('1234 456 789', False),
    ('123 4566 789', False),
    ('123 456 7899', False),
]


@pytest.mark.parametrize('text, chars', strip_test_data)
def test_strip_on_test_data(text, chars):
    assert regex.strip(text, chars) == text.strip(chars)


@pytest.mark.parametrize('password, is_valid', password_test_data)
def test_is_password_strong_on_test_data(password, is_valid):
    assert regex.is_password_strong(password) is is_valid


@pytest.mark.parametrize('email_address, is_valid', email_test_data)
def test_is_valid_email_address_on_test_data(email_address, is_valid):
    assert regex.is_valid_email_address(email_address) is is_valid


@pytest.mark.parametrize(
    'postal_code, kind, is_valid',
    postal_code_test_data)
def test_is_valid_postal_code_on_test_data(postal_code, kind, is_valid):
    assert regex.is_valid_postal_code(postal_code, kind) is is_valid


@pytest.mark.parametrize('phone_number, is_valid', mobile_phone_test_data)
def test_is_valid_mobile_phone_number_on_test_data(phone_number, is_valid):
    assert regex.is_valid_mobile_phone_number(phone_number) is is_valid
