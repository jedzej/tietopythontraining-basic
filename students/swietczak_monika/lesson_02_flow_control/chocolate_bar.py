# Read an integer:
n = int(input("Length of the chocolate bar: "))
m = int(input("Width of the chocolate bar: "))
k = int(input("How many squares should be after breaking the bar: "))
# Print a value:
# print(a)

if ((k % m == 0) or (k % n == 0)) and (k < m * n):
    print("YES")
else:
    print("NO")
