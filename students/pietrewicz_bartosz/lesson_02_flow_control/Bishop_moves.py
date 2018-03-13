# Read start (x1,y1) and end (x2,y2) coordinates
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Calculate if bishop can go from (x1,y1) to (x2,y2) in one move
if abs(x2-x1) == abs(y2-y1):
    print("YES")
else:
    print("NO")
