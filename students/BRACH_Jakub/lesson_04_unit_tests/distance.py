import pytest
from math import sqrt, pow


def distance(x1, y1, x2, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)) 

def test_TypeError_case():
    with pytest.raises(TypeError):
        distance()

def test_ValueError_case():
    with pytest.raises(ValueError):
        distance("aoeu")

def test_Negative_Coordinates():
    assert distance(-2, -2, -1, -1) == sqrt(2)
def 