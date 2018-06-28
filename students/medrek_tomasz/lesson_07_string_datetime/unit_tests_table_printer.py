import pytest
from table_printer import print_table


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

expected_table_data = '''  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

one_line = ['apples', 'oranges', 'cherries', 'banana']

expected_one_line = '''  apples
 oranges
cherries
  banana
'''

one_elem_missing = [['apples', 'oranges', 'cherries', 'banana'],
                    ['Alice', 'Carol', 'David'],
                    ['dogs', 'cats', 'moose', 'goose']]


expected_one_elem_missing = '''  apples Alice  dogs
 oranges Carol  cats
cherries David moose
  banana       goose
'''

one_elem_null = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', '', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]


expected_one_elem_null = '''  apples Alice  dogs
 oranges        cats
cherries Carol moose
  banana David goose
'''

numbers = [[1, 2, 3, 4],
           [5, 106, 7, 8]]

expected_numbers = '''1   5
2 106
3   7
4   8
'''


@pytest.mark.parametrize("test_input, expected", [
    (table_data, expected_table_data),
    (one_line, expected_one_line),
    (one_elem_missing, expected_one_elem_missing),
    (one_elem_null, expected_one_elem_null),
    (numbers, expected_numbers),
])
def test_eval(test_input, expected, capsys):
    print_table(test_input)
    out, err = capsys.readouterr()
    assert out == expected
