n = int(input("Give number: "))
factn = 1

for i in range(1, n + 1):
    factn = factn * i


print("The factorial of ", n, "is", factn)
