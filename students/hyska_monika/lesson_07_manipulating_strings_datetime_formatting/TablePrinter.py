# function print table with each column right-justified

from functions_lesson07 import print_table, find_max_sting


def change_row_to_columns(my_dict):
    new_dict = [[0] * len(my_dict) for i in range(len(my_dict[0]))]
    for i in range(len(my_dict[0])):
        for j in range(len(my_dict)):
            new_dict[i][j] = my_dict[j][i]
    return new_dict


tableData = [['apples', 'orange', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print('Table:')
print_table(tableData, find_max_sting(tableData))
print('\nTable changed:')
print_table(change_row_to_columns(tableData), find_max_sting(tableData))
