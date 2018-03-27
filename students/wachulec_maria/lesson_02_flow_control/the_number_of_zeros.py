N = int(input("N: "))
zeros_amount = 0
for i in range(N):
    number = int(input("Give me number: "))
    if number == 0:
        zeros_amount += 1
print(zeros_amount)
