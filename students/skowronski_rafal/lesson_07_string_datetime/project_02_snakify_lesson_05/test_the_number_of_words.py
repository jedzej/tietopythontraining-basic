import the_number_of_words
import pytest


test_data = [
    ('Hello world', 2),
    ('Hello', 1),
    ('q w e', 3),
    ('In the hole in the ground there lived a hobbit', 10),
    ('One two three four five', 5)
]


@pytest.mark.parametrize('text, expected_words_count', test_data)
def test_get_words_count_on_test_data(text, expected_words_count):
    assert the_number_of_words.get_words_count(text) == expected_words_count
