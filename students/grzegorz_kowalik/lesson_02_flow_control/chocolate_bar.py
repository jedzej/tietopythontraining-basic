rows = int(input())
cols = int(input())
k = int(input())

if k > rows * cols:
    print("NO")
elif k % cols == 0 or k % rows == 0:
    print("YES")
else:
    print("NO")
