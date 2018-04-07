import pytest
from the_bowling_alley import get_sequence_string


class TestTheBowlingAlley():
    test_data = [
        (10, [(8, 10), (2, 5), (3, 6)], 'I.....I...'),
        (5, [(1, 2), (4, 4)], '..I.I'),
        (10, [(3, 5), (4, 6), (10, 10)], 'II....III.'),
        (5, [], 'IIIII'),
        (5, [(5, 5), (5, 5), (3, 3), (1, 1), (2, 2), (4, 4)], '.....'),
        (20, [(1, 20)], '....................'),
        (20, [(3, 8), (13, 17), (6, 9)], 'II.......III.....III'),
        (15, [(1, 1), (1, 4), (6, 8), (7, 9)], '....I....IIIIII')
    ]

    @pytest.mark.parametrize('pins, pairs, expected', test_data)
    def test_get_sequence_string_on_test_data(self, pins, pairs, expected):
        assert get_sequence_string(pins, *pairs) == expected
