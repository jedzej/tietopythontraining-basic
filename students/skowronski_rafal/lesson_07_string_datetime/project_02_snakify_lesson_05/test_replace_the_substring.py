import replace_the_substring
import pytest


test_data = [
    ('1+1=2', 'one+one=2'),
    ('Hello, 2345678990', 'Hello, 2345678990'),
    ('1', 'one'),
    ('1111111111111111111111111111111111',
     'oneoneoneoneoneoneoneoneoneoneoneoneoneoneoneone' +
     'oneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneone'),
    ('1213141516171819101', 'one2one3one4one5one6one7one8one9one0one')
]


@pytest.mark.parametrize('text, expected', test_data)
def test_get_one_replaced_string_on_test_data(text, expected):
    assert replace_the_substring.get_one_replaced_string(text) == expected
