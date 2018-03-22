# Statement
# Chess knight moves like the letter L.
# It can move two cells horizontally and one cell vertically,
# or two cells vertically and one cells horizontally.
# Given two different cells of the chessboard,
# determine whether a knight can go from the first cell to the
#  second in one move.
# The program receives the input of four numbers from 1 to 8,
# each specifying the column and row number, first two - for the
#  first cell,
# and then the last two - for the second cell.
# The program should output YES if a knight can go
# from the first cell to the second in one move, or NO otherwise.


def knight_can_move():
    print("Enter two squares co-ordinates (1-8 numbers):")
    print("Starting square column:")
    a = int(input())
    print("Starting square row:")
    b = int(input())
    print("Ending square column:")
    c = int(input())
    print("Ending square row:")
    d = int(input())
    print("Can knight go from the first square to the second in one move?")
    x = abs(a - c)
    y = abs(b - d)
    if (x == 1 and y == 2) or (x == 2 and y == 1):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    knight_can_move()
