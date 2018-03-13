"""
Chocolate bar has the form of a rectangle divided into n×m portions.
Chocolate bar can be split into two rectangular parts by breaking it
along a selected straight line on its pattern. D
etermine whether it is possible to split it so that
one of the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO.
"""

print("Please input x size of chocolate bar:")
chocolate_x = int(input())
print("Please input x size of chocolate bar:")
chocolate_y = int(input())
print("Please input number of squares on the split part:")
squares = int(input())
if ((squares % chocolate_x == 0 or squares % chocolate_y == 0)
        and chocolate_x * chocolate_y > squares):
    print("YES")
else:
    print("NO")
