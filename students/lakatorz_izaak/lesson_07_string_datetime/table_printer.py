 # Write a function named printTable() that takes a list of lists of strings
 # and displays it in a well-organized table with each column right-justified.


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(param_list):
    col_widths = [0] * len(param_list)
    i = 0
    for string_list in param_list:
        col_widths[i] = len(max(string_list, key=len))
        i += 1

    for c in range(len(param_list[0])):
        for j in range(len(col_widths)):
            print(str(param_list[j][c]).rjust(col_widths[j]), end='  ')
        print()

printTable(tableData)