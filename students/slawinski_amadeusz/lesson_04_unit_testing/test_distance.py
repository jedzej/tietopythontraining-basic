#!/usr/bin/env python3

import math
import pytest


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(float(x2) - float(x1), 2) +
                     math.pow(float(y2) - float(y1), 2))


def test_TypeError_with_None():
    with pytest.raises(TypeError):
        distance(None, 0, 0, 0)


def test_ValueError_with_aoeu():
    with pytest.raises(ValueError):
        distance('a', 'o', 'e', 'u')


def test_ZeroLength():
    assert distance(0, 0, 0, 0) == 0
    assert distance(1, 1, 1, 1) == 0
    assert distance(1, -1, 1, -1) == 0
    assert distance(-1, 1, -1, 1) == 0
    assert distance(-1, -1, -1, -1) == 0


def test_NegativeCoordinates():
    assert distance(-1, -2, -1, -1) == 1
    assert distance(-3, -1, -1, -1) == 2
    assert distance(-1, -1, -4, -1) == 3
    assert distance(-1, -1, -1, -5) == 4


def test_VerticalDistance():
    assert distance(0, 1, 0, 2) == 1
    assert distance(0, 2, 0, 1) == 1


def test_HorizontalDistance():
    assert distance(1, 0, 2, 0) == 1
    assert distance(2, 0, 1, 0) == 1


def test_MixedCoordinates():
    assert distance(2, 1, 3, 1) == 1
    assert distance(2, 1, -3, 1) == 5
    assert distance(-2, 1, 3, 1) == 5
    assert distance(-2, 1, -3, 1) == 1
    assert distance(2, 3, 2, 4) == 1
    assert distance(2, 3, 2, -4) == 7
    assert distance(2, -3, 2, 4) == 7
    assert distance(2, -3, 2, -4) == 1


def test_PointsOrder():
    assert distance(0, 1, 2, 3) == distance(2, 3, 0, 1)
    assert distance(0, -1, -2, -3) == distance(-2, -3, 0, -1)
