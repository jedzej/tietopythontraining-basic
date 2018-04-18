n = int(input("X: "))
m = int(input("Y: "))
k = int(input("Number of squares in one part: "))

if n * m % k == 0 and n * m >= k:
    print("Yes")
else:
    print("No")
