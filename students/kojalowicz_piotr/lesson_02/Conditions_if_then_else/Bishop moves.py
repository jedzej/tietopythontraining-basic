rowFrom = int(input())
columnFrom = int(input())
rowTo = int(input())
columnTo = int(input())
if abs(rowFrom - rowTo) == abs(columnFrom - columnTo):
    print("YES")
else:
    print("NO")