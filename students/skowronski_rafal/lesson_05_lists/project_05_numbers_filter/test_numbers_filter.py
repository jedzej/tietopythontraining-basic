import pytest
from numbers_filter import get_filtered_array


class TestNumbersFilter:
    test_data = [
        (
            ['2', '0', '8', '3'],
            range(3),
            [8, 3],
        ),
        (
            ['2', '0', '8', '3', '1', '2', '3'],
            range(2, 3),
            [0, 8, 3, 1, 3]
        ),
        (
            ['2', '0', '8', '3', '1', '2', '3'],
            [0, 8],
            [2, 3, 1, 2, 3],
        ),
        (
            ['1', '2', '3', '4', '5', '6', '7'],
            [1, 3, 5, 7],
            [2, 4, 6]
        ),
        (
            ['1', '2', '3', '4', '5', '6', '7'],
            [],
            [1, 2, 3, 4, 5, 6, 7]
        ),
        (
            ['1', '2', '3', '4', '5', '6', '7'],
            [1, 2, 3, 4, 5, 6, 7],
            []
        ),
        (
            ['1', '2', '3', '4', '5', '6', '7'],
            [7, 6, 5, 4, 3, 2, 1],
            []
        ),
    ]

    @pytest.mark.parametrize('array, range, expected', test_data)
    def test_get_filtered_array_on_test_data(self, array, range, expected):
        assert get_filtered_array(array, range) == expected
