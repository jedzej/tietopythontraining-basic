from math import floor

A = int(input("Dollars (A): "))
B = int(input("Cents (B): "))
N = int(input("Amount (N): "))

all_cents_one_cupcake = A * 100 + B
price_n_cupcake = all_cents_one_cupcake * N
dollars = floor(price_n_cupcake / 100)
cents = price_n_cupcake - (dollars * 100)
print(dollars, cents)
