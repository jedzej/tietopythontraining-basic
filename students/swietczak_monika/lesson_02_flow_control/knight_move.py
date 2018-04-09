# Read an integer:
x1 = int(input("Enter x1 "))
y1 = int(input("Enter y1 "))
x2 = int(input("Enter x2 "))
y2 = int(input("Enter y2 "))
# Print a value:
# print(a)
result = "NO"
if abs(x1 - x2) == 2:
    if abs(y1 - y2) == 1:
        result = "YES"
    else:
        result = "NO"
if abs(y1 - y2) == 2:
    if abs(x1 - x2) == 1:
        result = "YES"
    else:
        result = "NO"
print(result)
