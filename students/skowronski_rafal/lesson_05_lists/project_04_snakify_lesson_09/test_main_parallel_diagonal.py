import pytest
from main_parallel_diagonal import get_matrix


class TestMainParallelDiagonal:
    test_data = [
        (1, [
            [0],
        ]),

        (2, [
            [0, 1],
            [1, 0]
        ]),

        (3, [
            [0, 1, 2],
            [1, 0, 1],
            [2, 1, 0],
        ]),

        (4, [
            [0, 1, 2, 3],
            [1, 0, 1, 2],
            [2, 1, 0, 1],
            [3, 2, 1, 0],
        ]),

        (5, [
            [0, 1, 2, 3, 4],
            [1, 0, 1, 2, 3],
            [2, 1, 0, 1, 2],
            [3, 2, 1, 0, 1],
            [4, 3, 2, 1, 0],
        ]),

        (6, [
            [0, 1, 2, 3, 4, 5],
            [1, 0, 1, 2, 3, 4],
            [2, 1, 0, 1, 2, 3],
            [3, 2, 1, 0, 1, 2],
            [4, 3, 2, 1, 0, 1],
            [5, 4, 3, 2, 1, 0],
        ]),

        (7, [
            [0, 1, 2, 3, 4, 5, 6],
            [1, 0, 1, 2, 3, 4, 5],
            [2, 1, 0, 1, 2, 3, 4],
            [3, 2, 1, 0, 1, 2, 3],
            [4, 3, 2, 1, 0, 1, 2],
            [5, 4, 3, 2, 1, 0, 1],
            [6, 5, 4, 3, 2, 1, 0]
        ]),
    ]

    @pytest.mark.parametrize('matrix_size, expected', test_data)
    def test_get_matrix_on_test_data(self, matrix_size, expected):
        assert get_matrix(matrix_size) == expected
