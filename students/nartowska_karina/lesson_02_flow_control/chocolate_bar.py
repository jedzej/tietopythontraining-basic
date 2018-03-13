# Chocolate bar has the form of a rectangle divided into n×m portions.
m = int(input())
n = int(input())
k = int(input())
if k % m == 0 or k % n == 0:
    print("YES")
else:
    print("NO")
