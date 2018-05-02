maximum = 0
sum = 0

while True:
    n = int(input("Number: "))
    if n == 0:
        break
    if n > maximum:
        maximum, sum = n, 1
    elif n == maximum:
        sum += 1


print("Number of maximum is: ", sum)
