row = int(input())
column = int(input())
noChocolateParts = int(input())
if noChocolateParts <= row * column:
    if (noChocolateParts % row == 0) or (noChocolateParts % column == 0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")