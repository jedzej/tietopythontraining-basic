def print_table(some_table):
    maxlens_table = []
    for i in some_table:
        maxlen = 0
        for elem in i:
            # print(elem)
            if len(elem) >= maxlen:
                maxlen = len(elem)
        maxlens_table.append(maxlen)
    print(maxlens_table)

    for i in range(len(some_table[0])):
        for j in range(len(some_table)):
            print(some_table[j][i].rjust(maxlens_table[j]), end=" ")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
