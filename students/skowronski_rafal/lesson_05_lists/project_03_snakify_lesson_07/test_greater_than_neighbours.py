import pytest
from greater_than_neighbours import get_number_of_elements


class TestGreaterThanNeighbours():
    test_data = [
        ('1 2 3 4 5', 0),
        ('5 4 3 2 1', 0),
        ('1 5 1 5 1', 2),
        ('5 1 5 1 5', 1),
        ('5 5 5 5 5', 0),
        ('1 1 1 5 1', 1),
        ('345354', 0),
        ('1 465', 0),
        ('4 -54643', 0),
        ('2147483647 0 1 2 3', 0),
        ('1 2 3 4 -2147483648', 1),
        ('-9 29 -100 64 26 73 -96 28 -92 11 -14 -86 -54 -67', 6),
        ('2147483647 0 1 0 2147483647', 1)
    ]

    @pytest.mark.parametrize('elements, expected', test_data)
    def test_get_number_of_elements_on_test_data(self, elements, expected):
        assert get_number_of_elements(elements.split()) == expected
