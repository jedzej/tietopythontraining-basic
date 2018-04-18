n = int(input("quantity of numbers: "))
zero = 0
for i in range(1, n + 1):
    i = int(input())
    if i == 0:
        zero += 1
print("Number of zeros: ", zero)
