import pytest
from age_calculator import age_calculator


@pytest.mark.parametrize("test_input, expected", [
    ([2, 20, 8, 32], (26, 2)),
    ([2, 0, 8, 3], (0, 3)),
    ([2, -10, 8, 3, 20], (20, 3)),
])
def test_eval(test_input, expected):
    assert age_calculator(test_input) == expected


def test_character_in_input_list():
    with pytest.raises(TypeError):
        age_calculator(['a', 0, 8, 3])
