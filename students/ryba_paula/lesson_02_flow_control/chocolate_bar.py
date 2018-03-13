n, m, squares = int(input()), int(input()), int(input())

portions = n * m

if squares < portions and ((squares % n == 0) or (squares % m == 0)):
    print("YES")
else:
    print("NO")
