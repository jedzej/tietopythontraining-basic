"""
Write a function named printTable() that takes a list of
lists of strings and displays it in a well-organized table
with each column right-justified. Assume that all
the inner lists will contain the same number of strings.
For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
"""


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    max_length = [0] * len(table_data)
    for i in range(len(table_data)):
        for j in table_data[i]:
            if len(j) > max_length[i]:
                max_length[i] = len(j)

    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(max_length[j]), end=' ')
        print()


if __name__ == '__main__':
    main()
