tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def table_printer(table):
    shapes = [len(max(i, key=len)) for i in table]
    print(shapes)
    for i in range(len(table[0])):
        for k in range(len(table)):
            print(table[k][i].rjust(shapes[k]), end=' ')
        print()


def main():
    table_printer(tableData)


if __name__ == '__main__':
    main()
