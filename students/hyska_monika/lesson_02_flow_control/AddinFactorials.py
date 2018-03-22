# Program print sum for n!

n = int(input("Put number: "))
fact = 1
sum_fact = 0

for i in range(1, n+1):
    fact = fact * i
    sum_fact += fact

print("Factorials sum is =", sum_fact)
