#Statement
#In chess, the bishop moves diagonally, any number of squares.
#Given two different squares of the chessboard, determine whether 
#a bishop can go from the first to the second in one move.
#The program receives as input four numbers from 1 to 8, 
#specifying the column and row numbers of the starting square 
#and the column and row numbers of the ending square. 
#The program should output YES if a Bishop can go from the first square
# to the second in one move, or NO otherwise.

def BishopCanMove():
    print("Enter two squares co-ordinates (1-8 numbers):")
    print("Starting square column:")
    a = int(input())
    print("Starting square row:")
    b = int(input())
    print("Ending square column:")
    c = int(input())
    print("Ending square row:")
    d = int(input())
    print("Can bishop go from the first square to the second in one move?")
    if(abs(a - c) == abs(b - d)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    BishopCanMove()