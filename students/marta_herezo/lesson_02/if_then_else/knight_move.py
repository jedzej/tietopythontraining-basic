# The program directed corrected or not corrected move
# of bishop on the chessboard.
# (x0, y0) - start position, (x, y) - new position on the chessboard.

print('Enter start posiotion for bishop, column x0: ')
x0 = int(input())

print('row y0: ')
y0 = int(input())

print('New position for bishop, column x: ')
x = int(input())

print('and row y: ')
y = int(input())

# move for x
x1 = x0 - x

# move for y
y1 = y0 - y

if abs(x1) != abs(y1) and abs(x1) == 2:
    print('YES')
elif abs(x1) != abs(y1) and abs(y1) == 2:
    print('YES')
else:
    print('NO')
