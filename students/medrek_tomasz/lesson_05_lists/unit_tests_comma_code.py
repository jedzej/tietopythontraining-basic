import pytest
from comma_code import comma_code


@pytest.mark.parametrize("test_input, expected", [
    (['apples', 'bananas', 'tofu', 'cats'], 'apples, bananas, tofu and cats'),
    (['1', '2', '3', '4'], '1, 2, 3 and 4'),
    (['', '', '', ''], ', ,  and '),
    (['1', '2'], '1 and 2'),
    (['1'], '1'),
])
def test_eval(test_input, expected):
    assert comma_code(test_input) == expected


def test_none():
    with pytest.raises(TypeError):
        comma_code(None)
