# This program takes a knights current position on the chessboard, and determines
#if it is legal to move to another given position on the chessboard
print("enter current position A")
currentA = int(input())
print("enter current position B")
currentB = int(input())
print("enter next position A")
nextA = int(input())
print("enter next position B")
nextB = int(input())

if ((abs(currentB - nextB)) == 2) and (abs(currentA - nextA) == 1):
    print("yes")
elif ((abs(currentB - nextB)) == 1) and (abs(currentA - nextA) == 2):
    print("yes")
else:
    print("no")
