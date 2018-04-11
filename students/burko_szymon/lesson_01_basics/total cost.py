A = int(input("Dollars: "))
B = int(input("Cents:"))
N = int(input("Number of cupcakes: "))

totalcost = (100 * A + B )* N

print("Total cost for delicious cupcakes; " + str(totalcost // 100) + " "  + str(totalcost % 100))

