rowFrom = int(input())
columnFrom = int(input())
rowTo = int(input())
columnTo = int(input())
if (rowFrom == rowTo) or (columnFrom == columnTo):
    print("YES")
elif abs(rowFrom - rowTo) == abs(columnFrom - columnTo):
    print("YES")
else:
    print("NO")