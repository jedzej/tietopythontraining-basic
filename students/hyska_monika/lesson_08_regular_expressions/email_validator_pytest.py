import pytest
from email_validator import check_email


# ********* tests for valid emails *********
@pytest.mark.parametrize("args", [
    'anaddd@gmail.com',
    'a@gmail.com',
    '432423@gmail.com',
    'AnsSisfd.sf78767sa@gmail.com',
    'anaddd@gmaxxxxxxxxxxil.com'
])
def test_valid_string_arguments(args):
    assert check_email(args) is True


# ********* tests for invalid emails *********
@pytest.mark.parametrize("args", [
    'anisfd.sf78767sagmail.com',
    'anisfd.sf78767sa@gmailcom',
    'anisfd.sf78767sa@g',
    'anisfd.sf78767sa@.com',
    'anisfd.sf78767sa@.',
    'a@g',
    'anisfd.sf78kk',
    'anisfd.sf78kk@dasmda.comcom',
    'sdsssssssssssssssssssss78767sa@gmaisssssssssssssl.cssssssssssom'
])
def test_invalid_string_arguments(args):
    assert check_email(args) is False
