# Read an integer:
dollars = int(input("How many dollars a cupcake costs: "))
cents = int(input("How many cents a cupcake costs: "))
n = int(input("How many cupcakes you buy: "))

sum_of_dollars = dollars * n + (cents * n) // 100
sum_of_cents = (cents * n) % 100
print(str(sum_of_dollars) + " " + str(sum_of_cents))
