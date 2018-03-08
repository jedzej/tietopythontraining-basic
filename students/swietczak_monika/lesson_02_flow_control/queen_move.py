# Read an integer:
a = int(input("Enter x1: "))
b = int(input("Enter y1: "))
c = int(input("Enter x2: "))
d = int(input("Enter y2: "))

if abs(a - c) == abs(b - d):
    print("YES")
elif (a == c) or (b == d):
    print("YES")
else:
    print("NO")
