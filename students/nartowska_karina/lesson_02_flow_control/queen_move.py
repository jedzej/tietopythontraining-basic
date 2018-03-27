c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if abs(r1 - r2) == abs(c1 - c2) or (r1 == r2) or (c1 == c2):
    print("YES")
else:
    print("NO")
