#Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two #rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is #possible to split it so that one of the parts will have exactly k squares.
#The program reads three integers: n, m, and k. It should print YES or NO. 

#------------------ 

#Desired chocolate pieces will be possible to get if:
#1. their number is not greater than the number of pieces in chocolate.
#2. their numbers depends on either the horisontal (k*n) or vertical (k*m) line
#   of division and is an integer (you cannot get a piece of a piece).

import sys

print("Enter chocolate width:")
n = int(input())

print("Enter chocolate heigth:")
m = int(input())

print("Enter desired chocolate pieces:")
k = int(input())

#1.
if k > m*n :
    print("NO")
    sys.exit()

#2.
if (k%n == 0) or (k%m == 0):
    print("YES")
else:
    print("NO")
