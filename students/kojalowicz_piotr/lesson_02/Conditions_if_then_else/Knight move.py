rowFrom = int(input())
columnFrom = int(input())
rowTo = int(input())
columnTo = int(input())
if abs(rowFrom - rowTo) == 2:
    if abs(columnFrom - columnTo) == 1:
        print("YES")
    else:
        print("NO")
elif abs(rowFrom - rowTo) == 1:
    if abs(columnFrom - columnTo) == 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
