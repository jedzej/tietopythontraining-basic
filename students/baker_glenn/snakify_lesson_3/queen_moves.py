# This program takes a queens current position on the chessboard, and determines
#if it is legal to move to another given position on the chessboard
print("enter current position A")
currentA = int(input())
print("enter current position B")
currentB = int(input())
print("enter next position A")
nextA = int(input())
print("enter next position B")
nextB = int(input())

if (abs(currentB - nextB)) == abs((currentA - nextA)):
    print("yes")
elif ((currentB - nextB) == 0) or ((currentA - nextA) == 0):
    print("yes")
else:
    print("no")
