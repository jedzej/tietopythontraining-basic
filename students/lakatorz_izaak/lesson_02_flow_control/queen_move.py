# Chess queen moves horizontally, vertically or diagonally to any number of
# cells. Given two different cells of the chessboard, determine whether a
# queen can go from the first cell to the second in one move.


print("Enter starting column")
column_start = int(input())

print("Enter starting row")
row_start = int(input())

print("Enter destination column")
column_dest = int(input())

print("Enter destination row")
row_dest = int(input())

if abs(column_start - column_dest) == abs(row_start - row_dest) or \
        column_start == column_dest or \
        row_start == row_dest:
    print('YES')
else:
    print("NO")
