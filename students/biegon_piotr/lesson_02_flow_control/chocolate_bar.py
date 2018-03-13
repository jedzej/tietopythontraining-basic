print("Chocolate bar\n")

n = int(input("Enter the number of portions along the chocolate bar: "))
m = int(input("Enter the number of portions across the chocolate bar: "))
k = int(input("Enter the number of portions you want to divide the chocolate bar into: "))

print("\nIs it possible to divide the chocolate bar so that one part has exactly {:d} squares?".format(k))

if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
    print('YES')
else:
    print('NO')
