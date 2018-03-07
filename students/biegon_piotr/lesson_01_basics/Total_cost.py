print("Total cost\n")

A = int(input("Enter the cost in dollars: "))
B = int(input("Enter how many cents: "))
N = int(input("Enter the number of cupcakes: "))

sum_in_cents = int((A * 100 + B) * N)

print("\nTotal cost for %d cupcakes in dollars and cents is " + str(sum_in_cents // 100) + " " + str(sum_in_cents % 100))