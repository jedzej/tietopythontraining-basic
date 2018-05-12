# This program returns two numbers: total cost in dollars and cents.

A = int(input("Put how many dollars cost cupcake: "))
B = int(input("and how many cents: "))
N = int(input("Put how many cupcake you will buy: "))

dollars = A * N + B * N // 100
cents = (B * N) % 100
print("Total cost is:", dollars, "dollars and ", cents, "cents.")
