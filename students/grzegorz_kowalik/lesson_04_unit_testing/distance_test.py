import pytest
from students.grzegorz_kowalik.lesson_03_functions import distance


def test_type_error():
    with pytest.raises(TypeError):
        distance.distance(None, 1, 1, 1)


def test_value_error():
    with pytest.raises(TypeError):
        distance.distance('aoeu', 1, 1, 1)


def test_zero_len():
    assert 0 == distance.distance(1, 1, 1, 1)


def test_negative_coords():
    assert 2 == distance.distance(-1, 0, 1, 0)


def test_only_vertical():
    assert 5 == distance.distance(0, 0, 0, 5)


def test_only_horizontal():
    assert 5 == distance.distance(0, 0, 5, 0)
