import pytest
import sort


test_data = [
    ((1, 4, -2, 2), [-2, 1, 2, 4]),
    ((-1, 111, 1, 0), [-1, 0, 1, 111])
]


@pytest.mark.parametrize('input, output', test_data)
def test_to_list_on_test_data(input, output):
    assert sort.to_list(*input) == output
