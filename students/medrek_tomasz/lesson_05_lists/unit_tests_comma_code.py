import pytest
from comma_code import comma_code


@pytest.mark.parametrize("test_input,expected", [
    ("comma_code(['apples', 'bananas', 'tofu', 'cats'])",
     'apples, bananas, tofu and cats'),
    ("comma_code(['1', '2', '3', '4'])",
     '1, 2, 3 and 4'),
    ("comma_code(['', '', '', ''])",
     ', ,  and '),
    ("comma_code(['1', '2'])",
     '1 and 2'),
    ("comma_code(['1'])",
     '1'),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


def test_none():
    with pytest.raises(TypeError):
        comma_code(None)
