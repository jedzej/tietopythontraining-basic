def print_table(some_table):
    max_length_table = []
    for i in some_table:
        max_length = 0
        for elem in i:
            if len(elem) >= max_length:
                max_length = len(elem)
        max_length_table.append(max_length)

    for i in range(len(some_table[0])):
        for j in range(len(some_table)):
            print(some_table[j][i].rjust(max_length_table[j]), end=" ")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
