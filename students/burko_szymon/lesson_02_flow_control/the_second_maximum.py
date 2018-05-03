maximum = 0
second_maximum = 0

while True:
    n = int(input("Number: "))
    if n == 0:
        break
    if n > maximum:
        second_maximum, maximum = maximum, n
    elif n > second_maximum:
        second_maximum = n
print("Second maximum is: ", second_maximum)
