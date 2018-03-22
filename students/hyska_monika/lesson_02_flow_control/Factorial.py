# Program print value for n!

n = int(input("Put number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial is =", fact)
