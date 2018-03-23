# Statement
# Chess queen moves horizontally, vertically or diagonally to any
# number of cells.
# Given two different cells of the chessboard, determine whether
#  a queen can go from
# the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8,
# each specifying the column and row number, first two - for the first cell,
# and then the last two - for the second cell.
# The program should output YES if a queen can go
# from the first cell to the second in one move, or NO otherwise.


def queen_can_move():
    print("Enter two squares co-ordinates (1-8 numbers):")
    print("Starting square column:")
    a = int(input())
    print("Starting square row:")
    b = int(input())
    print("Ending square column:")
    c = int(input())
    print("Ending square row:")
    d = int(input())
    print("Can queen go from the first square to the second in one move?")
    if(a == c or b == d or (abs(a - c) == abs(b - d))):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    queen_can_move()
