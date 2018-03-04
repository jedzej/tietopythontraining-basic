
maximum = 0
second_maximum = 0

while True:
    n = int(input("Integer: "))
    if n == 0:
        break
    if n > maximum:
        second_maximum = maximum
        maximum = n

    elif second_maximum < n < maximum:
        second_maximum = n

print(second_maximum)
