
n = int(input("Length of chocolate: "))
m = int(input("Width of chocolate "))
k = int(input("Number of squares: "))

if k > n*m:
    print("NO\n")
    exit()

chocolate_squares = 0
for row in range(n):
    chocolate_squares = chocolate_squares + m
    if chocolate_squares == k:
        break

if chocolate_squares == k:
    print('YES\n')
else:
    print('NO\n')
