import pytest
from TheLengthOfTheSegment import distance

def test_TypeError():
    with pytest.raises(TypeError):
        distance(None)

def test_valueError():
    with pytest.raises(TypeError):
        distance('aoeu', 1, 5, 4)

def test_ZeroLength():
    assert distance(0, 0, 0, 0) == 0
    assert distance(-5, -5, -5, -5) == 0
    assert distance(1.5, 1.5, 1.5, 1.5) == 0

def test_NegativeCoordinates():
    assert distance(-1, -1, -4, -5) == 5
    assert distance(-10.1, -10.1, -5.1, -5.1) == 7.0710678118654755

def test_VerticalDistance():
    assert distance(3, 3, 3, 10) == 7
    assert distance(-3, -3, -3, 3.5) == 6.5

def test_HorizontalDistance():
    assert distance(0, 5, 10, 5) == 10

def test_MixedCoordinates():
    assert distance(-2.5, 2.5, 0.5, 6.5) == 5
    assert distance(2, 2, 7.5, 5) == 6.264982043070834

def test_OrderOfPoints():
    assert distance(-2.5, 2.5, 0.5, 6.5) == distance(0.5, 6.5, -2.5, 2.5)
