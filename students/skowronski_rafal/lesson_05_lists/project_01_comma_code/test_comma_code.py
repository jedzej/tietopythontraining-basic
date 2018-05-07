import pytest
from comma_code import convert_to_comma_string


class TestCommaCode():
    test_data = [
        ([], ''),
        (['1'], '1'),
        (['a', 'b'], 'a, b'),
        (['a', 'b', 'c'], 'a, b, and c'),
        (['1', '2', '3'], '1, 2, and 3'),
        ([1, 2, 3], '1, 2, and 3'),
        (['apples', 'bananas', 'tofu', 'cats'],
            'apples, bananas, tofu, and cats')
    ]

    @pytest.mark.parametrize('array, expected', test_data)
    def test_convert_to_comma_string_on_test_data(self, array, expected):
        assert convert_to_comma_string(array) == expected
