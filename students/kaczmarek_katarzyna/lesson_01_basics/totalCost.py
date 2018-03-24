dollars = int(input("Dollars (for 1 cupcake): "))
cents = int(input("Cents (for 1 cupcake): "))
cupcakes = int(input("Number of cupcakes: "))

total_cost = cupcakes * (dollars * 100 + cents)
print(total_cost // 100, total_cost % 100)
