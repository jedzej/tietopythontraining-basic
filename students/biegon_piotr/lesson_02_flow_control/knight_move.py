print("Knight move\n")

print("Enter the start coordinates:")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

print("\nEnter the final coordinates:")
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print("\nIs it possible to move the knight in one move to the coordinates given above?")

if x2 == x1 - 2 and (y2 == y1 + 1 or y2 == y1 - 1):
    print("YES")
elif x2 == x1 - 1 and (y2 == y1 + 2 or y2 == y1 - 2):
    print("YES")
elif x2 == x1 + 1 and (y2 == y1 + 2 or y2 == y1 - 2):
    print("YES")
elif x2 == x1 + 2 and (y2 == y1 + 1 or y2 == y1 - 1):
    print("YES")
else:
    print("NO")
