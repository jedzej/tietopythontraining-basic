a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a - c) == abs(b - d):
    print('YES')
elif a == c and b > d:
    print("YES")
elif a == c and b < d:
    print("YES")
elif a > c and b == d:
    print("YES")
elif a < c and b == d:
    print("YES")
else:
    print("NO")
