import pytest
from swap_min_and_max import swap


class TestSwapMinAndMax():
    test_data = [
        ('3 4 5 2 1', '3 4 1 2 5'),
        ('1 5 4 3 2', '5 1 4 3 2'),
        ('-30000 30000', '30000 -30000'),
        ('1', '1'),
        ('2147483647 -2147483648', '-2147483648 2147483647'),
        ('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 17 16 15 14',
         '18 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 1 17 16 15 14'),
        ('1 2 3 4 5 6 7 8 9 10', '10 2 3 4 5 6 7 8 9 1'),
        ('10 9 8 7 6 5 4 3 2 1', '1 9 8 7 6 5 4 3 2 10')
    ]

    @pytest.mark.parametrize('elements, expected', test_data)
    def test_swap_on_test_data(self, elements, expected):
        array = elements.split()
        swap(array)
        assert array == expected.split()
