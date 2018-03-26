a = int(input("price(dolar): "))
b = int(input("price(cent): "))
n = int(input("number of cupcake: "))

c = b * n

cent = c % 100
dolar = a * n + c / 100
print(str(dolar) + "  " + str(cent))
