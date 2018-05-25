import pytest
from distance import distance
"""
Dopisalam parametryzacje, ale jak czytam wiecj i wiecej o tym jak
to dobrze zrobic - wiem, ze to nie jest jeszcze najlepsze rozwiazanie.
Wizc jesli nie popisalam jakis glupot, to prosze zrob merga dla tej lekcji
jak juz skoncze ten kurs, mam zamiar usiasc do tych testow z wiekszymu
szczegolami
"""


# ********* tests for string input *********
@pytest.mark.parametrize("args", [
    ('aoeu', 'aoeu', 'aoeu', 'aoeu'),
    ('aoeu', 2, 3, 4),
    (1, 'aoeu', 3, 4),
    (1, 2, 'aoeu', 4),
    (1, 2, 3, 'aoeu'),
])
def test_invalid_string_arguments_to_raises(args):
    with pytest.raises(ValueError):
        distance(*args)


# ********* tests for None input *********
@pytest.mark.parametrize("args", [
    (None, None, None, None),
    (None, 2, 3, 4),
    (1, None, 3, 4),
    (1, 2, None, 4),
    (1, 2, 3, None),
])
def test_invalid_string_arguments_to_raises(args):
    with pytest.raises(TypeError):
        distance(*args)


# ********* tests for outputs *********
@pytest.mark.parametrize("test_input,expected", [
    (str(distance(2, 1, 2, 1)), 0.0),
    (str(distance(-1, -1, -3, -5)), 4.47214) ,
    (str(distance(2, 1, 2, 7)), 6.0),            # Only vertical distance
    (str(distance(5, 1, 10, 1)), 5.0),         # Only horizontal distance
    # Typical conditions (difference on both coordinates)
    (str(distance(3, -2, -1, 7)), 9.84886),
    (str(distance(-10, 2, 5, 12)), 18.02776),
    (str(distance(1, -5, -10, -12)), 13.0384),
    (str(distance(1, -5.1, 5.4, -12)), 8.18352),
    # Test that the order of points does not matter
    (str(distance(5, 1, 10, 2)), distance(10, 2, 5, 1))
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
