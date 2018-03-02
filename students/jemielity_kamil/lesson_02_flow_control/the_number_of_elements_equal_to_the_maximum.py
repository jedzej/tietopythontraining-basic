maximum = 0
counter = 0

while True:
    n = int(input("Integer: "))
    if n == 0:
        break
    if n > maximum:
        maximum = n
        counter = 1
    elif n == maximum:
        counter += 1

print(counter)

