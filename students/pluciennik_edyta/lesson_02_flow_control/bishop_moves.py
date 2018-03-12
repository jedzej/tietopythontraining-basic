a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < c and b < d and a + c == b + d: 
    print("YES")
elif a < c and b > d and a + b == c + d:
    print("YES")
elif a > c and b < d and a + b == c + d: 
    print("YES")
elif a > c and b > d and a + c == b + d: 
    print("YES")
else: 
    print("NO")
