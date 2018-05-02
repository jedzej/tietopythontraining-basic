"""In chess, the bishop moves diagonally, any number of squares. Given
two different squares of the chessboard, determine whether a bishop can
go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the
column and row numbers of the starting square and the column and row
numbers of the ending square. The program should output YES if a Bishop
can go from the first square to the second in one move, or NO otherwise."""

# Read an integer:
move_start_x = int(input())
move_start_y = int(input())

move_end_x = int(input())
move_end_y = int(input())

diff_equality = move_start_y - move_start_x == move_end_y - move_end_x
sum_equality = move_start_x + move_start_y == move_end_x + move_end_y

# Print a value:
if diff_equality or sum_equality:
    print('YES')
else:
    print('NO')
