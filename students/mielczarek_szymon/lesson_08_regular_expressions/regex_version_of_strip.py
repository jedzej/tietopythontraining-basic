#! python3
import re
import pytest


def my_strip(string, chars=''):
    """Regex version of strip()"""
    if not chars:
        regex = re.compile(r'^\s+|\s+$')
    else:
        regex = re.compile(r'^[{0}]*|[{0}]*$'.format(chars))
    return regex.sub('', string)


class TestMyStrip:
    @pytest.mark.parametrize("test_string", [
        ' python is awesome ',
        '   python is awesome  ',
        '   python  ',
        'python is awesome',
        '   python is awesome  ',
        '\rpython is awesome\r\r',
        '',
    ])
    def test_whitespace_chars(self, test_string):
        assert my_strip(test_string) == test_string.strip()

    @pytest.mark.parametrize("test_string,chars", [
        ('python is awesome', 'py'),
        ('python is awesome', 'p'),
        ('python is awesome', 'yt'),
        ('pypython is awesome pypypy', 'py'),
        ('python is awesome py py', 'py'),
        ('py', 'py'),
        ('y', 'py'),
        ('p', 'py'),
        (' ', 'py'),
        ('', 'py'),
        ('   python is awesome  ', ' '),
        ('\rpython is awesome\r\r', '\r'),
        ('++python is awesome+', '+'),
    ])
    def test_chars_parameter(self, test_string, chars):
        assert my_strip(test_string, chars) == test_string.strip(chars)
