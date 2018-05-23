import pytest
from distance import distance


def test_invalid_string_arguments_to_raises():
    with pytest.raises(ValueError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')
        distance('aoeu', 2, 3, 4)
        distance(1, 'aoeu', 3, 4)
        distance(1, 2, 'aoeu', 4)
        distance(1, 2, 3, 'aoeu')


def test_invalid_None_arguments_to_raises():
    with pytest.raises(TypeError):
        distance(None, None, None, None)
        distance(None, 2, 3, 4)
        distance(1, None, 3, 4)
        distance(1, 2, None, 4)
        distance(1, 2, 3, None)


def test_answer():
    assert distance(2, 1, 2, 1) == 0.0           # Zero length
    assert distance(-1, -1, -3, -5) == 4.47214   # Negative coordinates
    assert distance(2, 1, 2, 7) == 6.0           # Only vertical distance
    assert distance(5, 1, 10, 1) == 5.0          # Only horizontal distance
    # Typical conditions (difference on both coordinates)
    assert distance(3, -2, -1, 7) == 9.84886
    assert distance(-10, 2, 5, 12) == 18.02776
    assert distance(1, -5, -10, -12) == 13.0384
    assert distance(1, -5.1, 5.4, -12) == 8.18352
    # Test that the order of points does not matter
    assert distance(5, 1, 10, 2) == distance(10, 2, 5, 1)
