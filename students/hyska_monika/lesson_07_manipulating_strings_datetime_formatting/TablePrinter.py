# function print table with each column right-justified

from functions_lesson07 import find_max_stings_for_columns,\
    print_table2, find_max_stings_for_rows


def change_row_to_columns(my_dict):
    new_dict = [[0] * len(my_dict) for i in range(len(my_dict[0]))]
    for i in range(len(my_dict[0])):
        for j in range(len(my_dict)):
            new_dict[i][j] = my_dict[j][i]
    return new_dict


def change_row_to_columns2(table_data):
    new_table = map(list, zip(*table_data))
    return new_table


tableData = [['apples', 'orange', 'cherries', 'banana'],
             ['Alicess', 'Bob', 'Carol', 'David'],
             ['dogs', 'catssssss', 'moose', 'goose']]

print('Table:')
print_table2(tableData, find_max_stings_for_columns(tableData))
print('\nTable changed:')
print_table2(change_row_to_columns2(tableData),
             find_max_stings_for_rows(tableData))
