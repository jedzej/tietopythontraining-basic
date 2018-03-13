# Chocolate bar has the form of a rectangle divided into n×mn×m portions.
# Chocolate bar can be split into two rectangular parts by breaking it along
#  a selected straight line on its pattern. Determine whether it is possible
#  to split it so that one of the parts will have exactly k squares.

print("Enter n dimension")
n = int(input())

print("Enter m dimension")
m = int(input())

print("Enter number of squares (k)")
k = int(input())

if k % n == 0 or k % m == 0:
    if (n * m >= k):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
