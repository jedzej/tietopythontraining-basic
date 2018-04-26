# Given an integer n, produce a two-dimensional array of size (n×n) and
# complete it according to the following rules, and print with a single
# space between characters:

n = int(input('Enter n: '))

table = []

zero_index = 0

for i in range(n):
    row = []
    for j in range(n):
        row.append(abs(j - i))
    table.append(row)

for row in range(len(table)):
    print(table[row])
