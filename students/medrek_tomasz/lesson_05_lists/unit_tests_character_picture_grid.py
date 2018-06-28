import pytest
from character_picture_grid import transpose_matrix_and_ret_str


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

expected_grid = '''..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....'''

names = [['z', 'b', 'y', 's', 'z', 'e', 'k'],
         ['k', 'r', 'z', 'y', 's', 'i', 'o']]

expected_names = '''zk
br
yz
sy
zs
ei
ko'''

only_one_row = ['z', 'b', 'y', 's', 'z', 'e', 'k']

expected_only_one_row = '''z
b
y
s
z
e
k'''

one_row_is_bigger = [['z', 'b', 'y', 's', 'z', 'e', 'k'],
                     ['m', 'a', 'r', 'e', 'k']]

expected_one_row_is_bigger = '''zm
ba
yr
se
zk
e
k'''

one_collumn_is_bigger = [['z', 'm'],
                         ['b', 'a'],
                         ['y', 'r'],
                         ['s', 'e'],
                         ['z', 'k'],
                         ['e'],
                         ['k']]

expected_one_collumn_is_bigger = '''zbyszek
marek'''


@pytest.mark.parametrize("test_input, expected", [
    (grid, expected_grid),
    (names, expected_names),
    (only_one_row, expected_only_one_row),
    (one_row_is_bigger, expected_one_row_is_bigger),
    (one_collumn_is_bigger, expected_one_collumn_is_bigger)
])
def test_eval(test_input, expected):
    assert transpose_matrix_and_ret_str(test_input) == expected


def test_none_input():
    with pytest.raises(TypeError):
        transpose_matrix_and_ret_str(None)
