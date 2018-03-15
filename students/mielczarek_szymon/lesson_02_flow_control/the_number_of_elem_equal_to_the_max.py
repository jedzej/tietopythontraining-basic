maximum = 0
counter = 0
n = int(input())
while n != 0:
    if n > maximum:
        maximum, counter = n, 1
    elif n == maximum:
        counter += 1
    n = int(input())

print(counter)

