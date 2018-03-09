# Chocolate bar has the form of a rectangle divided into n×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern.
# Determine whether it is possible to split it so that one of the parts will have exactly k squares.

# The program reads three integers: n, m, and k. It should print YES or NO.

row_size = int(input())
column_size = int(input())
squares_nr = int(input())

result = 'NO'

for row_count in range(1, row_size):
    if squares_nr == row_count * column_size:
        result = 'YES'

if result == 'NO':
    for column_count in range(1, column_size):
        if squares_nr == column_count * row_size:
            result = 'YES'

print(result)
