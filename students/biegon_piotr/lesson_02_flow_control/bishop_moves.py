print("Bishop moves\n")

print("Enter the start coordinates:")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

print("\nEnter the final coordinates:")
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print("\nIs it possible to move the bishop in one move to the coordinates given above?")

if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
