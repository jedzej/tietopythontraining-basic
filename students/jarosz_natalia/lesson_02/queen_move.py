x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

dx = abs(x1 - x2)

dy = abs(y1 - y2)



if dx == dy:

    print("YES")

elif dx == 0 or dy ==0:

    print("YES")

else:

    print("NO")
