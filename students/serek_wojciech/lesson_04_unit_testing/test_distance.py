"""Unit tests for distance function using pytest"""
import pytest
from lesson_03_functions.length_of_the_segment import distance


def test_none():
    """Test for None value as parameter"""
    with pytest.raises(TypeError):
        distance(None, 'b', 'c', 'd')


def test_non_integer():
    """Test for no integer as parameter"""
    with pytest.raises(TypeError):
        distance('aoeu', 0, 1, 2)


def test_zero_length():
    """Test for zero distance"""
    assert distance(1, 1, 1, 1) == 0


def test_negative():
    """Test for negative coordinates"""
    assert distance(-1, -3, -5, -6) == 5.0


def test_only_vertical():
    """Test only vertical coordinates"""
    assert distance(1, 1, 1, 5) == 4


def test_only_horizontal():
    """Test only vertical coordinates"""
    assert distance(1, 1, 5, 1) == 4


def test_typical():
    """Test tupical coordinates"""
    assert distance(10, 15, 20, 5) == 14.142135623730951


def test_points_order():
    """Test that the order of points does not matter"""
    distance1 = distance(10, 15, 20, 5)
    distance2 = distance(20, 5, 10, 15)
    assert distance1 == distance2
