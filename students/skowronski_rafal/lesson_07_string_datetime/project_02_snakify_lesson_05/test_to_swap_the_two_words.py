import to_swap_the_two_words
import pytest


test_data = [
    ('Hello, world!', 'world! Hello,'),
    ('A B', 'B A'),
    ('Q WERRTYUIOP', 'WERRTYUIOP Q'),
    ('QWERTYUIOP M', 'M QWERTYUIOP'),
    ('sadfahsjkldfhasjkdfhaklsjdfhjkl asdlkfhasdjklfhaslkdfjhalskdfgalsdf',
     'asdlkfhasdjklfhaslkdfjhalskdfgalsdf sadfahsjkldfhasjkdfhaklsjdfhjkl')
]


@pytest.mark.parametrize('text, expected_text', test_data)
def test_get_swapped_string_on_test_data(text, expected_text):
    assert to_swap_the_two_words.get_swapped_string(text) == expected_text
