n = int((input("Enter length of rectangle: ")))
m = int((input("Enter width of rectangle: ")))
k = int((input("Enter amount of squares: ")))

all_squares = n*m
if (k <= all_squares) and ((k % n == 0) or (k % m == 0)):
    print ("YES")
else:
    print ("NO")
