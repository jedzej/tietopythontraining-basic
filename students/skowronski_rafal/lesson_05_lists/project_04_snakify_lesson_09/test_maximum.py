import pytest
from maximum import get_maximum_index


class TestMaximum:
    test_data = [
        ([
            [0, 3, 2, 4],
            [2, 3, 5, 5],
            [5, 1, 2, 3]
        ], (1, 2)),
        ([
            [1]
        ], (0, 0)),
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ], (2, 4)),
        ([
            [1],
            [2],
            [3],
            [2],
            [1],
            [2]
        ], (2, 0)),
        ([
            [1, 2, 3, 3, 2, 1]
        ], (0, 2)),
        ([
            [1, 4, 5, 2, 7],
            [3, 4, 8, 0, 8],
            [8, 8, 8, 8, 8]
        ], (1, 2)),
        ([
            [-3, -2],
            [-2, -1]
        ], (1, 1)),
        ([
            [-1000000003, -1000000002],
            [-1000000002, -1000000001]
        ], (1, 1))
    ]

    @pytest.mark.parametrize('matrix, expected', test_data)
    def test_get_maximum_index_on_test_data(self, matrix, expected):
        assert get_maximum_index(matrix) == expected
