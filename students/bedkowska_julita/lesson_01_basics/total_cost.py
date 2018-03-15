a = int(input())
b = int(input())
n = int(input())

totalCost = (100 * a + b) * n
dollars = totalCost // 100
cents = totalCost % 100

print("Total cost: "+str(dollars)+" "+str(cents))
