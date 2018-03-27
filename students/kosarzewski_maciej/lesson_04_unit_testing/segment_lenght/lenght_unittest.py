import pytest
import unittest
import lenght_of_segment


class LenghtTest(unittest.TestCase):
    def test_type_error_when_none(self):
        with pytest.raises(TypeError):
            lenght_of_segment.distance(None)

    def test_value_error_when_aoeu(self):
        with pytest.raises(TypeError):
            lenght_of_segment.distance("aoeu", 2, 2, 2)

    def test_zero_distance(self):
        self.assertEquals(lenght_of_segment.distance(3, 3, 3, 3), 0)

    def test_negative_coordinates(self):
        self.assertEquals(lenght_of_segment.distance(-1, -1, -3, -5), 4.47213595499958)

    def test_only_vertical(self):
        self.assertEquals(lenght_of_segment.distance(0, 5, 0, 7), 2)

    def test_only_horizontal(self):
        self.assertEquals(lenght_of_segment.distance(1, 3, 4, 3), 3)


if __name__ == '__main__':
    unittest.main()
