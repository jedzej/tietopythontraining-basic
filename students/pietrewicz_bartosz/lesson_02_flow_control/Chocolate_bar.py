# Read the size of chocolate bar
n = int(input())
m = int(input())
# Read the number of squares required after breaking the chocolate bar
k = int(input())
# Calculate if chocolate bar can be broken in a way that one part has
# exactly k squares
if (k < m*n) and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
