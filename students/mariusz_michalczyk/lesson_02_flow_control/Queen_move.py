x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

cond1 = (x1 == x2)
cond2 = (y1 == y2)
cond3 = ((abs(x2 - x1)) == (abs(y2 - y1)))

if cond1 or cond2 or cond3:
    print("YES")
else:
    print("NO")
