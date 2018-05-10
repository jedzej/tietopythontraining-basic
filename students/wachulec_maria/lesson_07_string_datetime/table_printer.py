def print_table(table):
    shapes = [len(max(i, key=len)) for i in table]
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(shapes[j]), end=' ')
        print()


TABLE_DATE = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(TABLE_DATE)
