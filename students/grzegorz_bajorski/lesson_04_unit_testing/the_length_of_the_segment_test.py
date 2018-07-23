import pytest
from the_length_of_the_segment import distance


class MyTest(pytest):

    def test_1(self):
        with pytest.raises(TypeError):
            distance(None, 1,  2, 3)

    def test_2(self):
        with pytest.raises(ValueError):
            distance('aoeu', 1, 2, 3)

    def test_3(self):
        assert distance(1, 1, 1, 1) == 0

    def test_4(self):
        assert distance(-1, -2, -3, -4) == 5

    def test_5(self):
        assert distance(1, 1, 1, 2) == 1

    def test_6(self):
        assert distance(1, 1, 2, 1) == 1

    def test_7(self):
        assert distance(5, 8, 2, 6) == 4

    def test_8(self):
        distance1 = distance(1, 2, 3, 4)
        distance2 = distance(3, 4, 1, 2)
        self.assertEqual(distance1, distance2)


if __name__ == "__main__":
    pytest.main()
