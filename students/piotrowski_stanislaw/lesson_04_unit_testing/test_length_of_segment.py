import pytest
from length_of_segment import distance
# from lesson_03_functions.length_of_segment import distance


class TestDistanceFunction(object):
    def test_none_as_input_parameter(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

    def test_string_as_input_parameter(self):
        with pytest.raises(TypeError):
            distance('aoeu', 'aoeu', 'aoeu', 'aoeu')

    def test_zero_length(self):
        assert distance(1, 1, 1, 1) == 0

    def test_negative_coordinates(self):
        assert distance(-3, -4, 0, 0) == 5

    def test_only_vertical_distance(self):
        assert distance(1, 3, 1, 6) == 3

    def test_only_horizontal_distance(self):
        assert distance(2, 2, 7, 2) == 5

    def test_order_of_points_matters(self):
        assert distance(3, 4, 7, 8) == distance(7, 8, 3, 4)
