# Statement
# Chocolate bar has the form of a rectangle divided into n×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it
# along a selected straight line on its pattern.
# Determine whether it is possible to split it so
# that one of the parts will have exactly k squares.
# The program reads three integers: n, m, and k. It should print YES or NO.


def chocolate_bar():
    print("Enter chocolate dimensions:")
    print("Width in cubes of chocolate:")
    a = int(input())
    print("Height in cubes of chocolate:")
    b = int(input())
    print("How many cubes you would like to eat:")
    c = int(input())
    print("Is it possible to split chocolate so that one of "
          "the parts will have exactly " + str(c) + " squares?")
    if ((c % b == 0 or c % a == 0) and c < a*b):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    chocolate_bar()
