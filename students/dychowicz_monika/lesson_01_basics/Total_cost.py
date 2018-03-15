a = int(input("Cupcake cost: "))
b = int(input("Dollars: "))
n = int(input("Cents: "))
print(a)
cost = n * (100 * a + b)
print(cost // 100, cost % 100)


