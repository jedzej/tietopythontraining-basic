def printTable(datatable):
    to_print = ''
    for i in range(len(datatable[0])):
        for j in range(len(datatable)):
            to_print = to_print + datatable[j][i] + ' '
        to_print = to_print + '\n '
    print(to_print)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
