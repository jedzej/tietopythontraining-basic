import table_printer
import pytest


test_data = [
    ([
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']],
        '  apples Alice  dogs\n' +
        ' oranges   Bob  cats\n' +
        'cherries Carol moose\n' +
        '  banana David goose')
    ]


@pytest.mark.parametrize('table_data, expected_string', test_data)
def test_get_printable_table_on_test_data(table_data, expected_string):
    assert table_printer.get_printable_table(table_data) == expected_string


@pytest.mark.parametrize('table_data, expected_string', test_data)
def test_get_printable_table_v2_on_test_data(table_data, expected_string):
    assert table_printer.get_printable_table_v2(table_data) == expected_string
