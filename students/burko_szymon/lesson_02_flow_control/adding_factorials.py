n = int(input("Give number: "))
factn = 1
factsum = 0
for i in range(1, n + 1):
    factn = factn * i
    factsum = factsum + factn
print("Factorials sum: ", factsum)
