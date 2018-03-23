X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())

cond1 = (abs(X1 - X2)) == 2 and (abs(Y1 - Y2) == 1)
cond2 = (abs(Y1 - Y2)) == 2 and (abs(X1 - X2) == 1)

if cond1 or cond2:
    print("YES")
else:
    print("NO")
