a = input("price(dolar): ")
b = input("price(cent): ")
n = input("number of cupcake: ")

c = b * n

cent = c%100
dolar = a * n + c/100
print (str(dolar) + "  " + str(cent))
