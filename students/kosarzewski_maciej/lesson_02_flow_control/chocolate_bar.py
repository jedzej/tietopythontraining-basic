x = int(input())
y = int(input())
part = int(input())
surface = x*y
if surface >= part and (surface-part == x or surface - part == y or x == part or y == part or
                        (surface-part) % x == 0 or (surface-part) % y == 0):
    print("YES")
else:
    print("NO")
