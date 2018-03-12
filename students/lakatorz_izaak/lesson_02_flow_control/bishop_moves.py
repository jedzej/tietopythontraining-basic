# In chess, the bishop moves diagonally, any number of squares. Given two
# different squares of the chessboard, determine whether a bishop can go
# from the first to the second in one move.


print("Enter starting column")
column_start = int(input())

print("Enter starting row")
row_start = int(input())

print("Enter destination column")
column_dest = int(input())

print("Enter destination row")
row_dest = int(input())

if abs(column_start - column_dest) == abs(row_start - row_dest):
    print('YES')
else:
    print("NO")
