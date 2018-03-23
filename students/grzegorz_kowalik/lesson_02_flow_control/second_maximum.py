maximum = 0
second_maximum = 0
n = 1

while n != 0:
    n = int(input())
    if n > maximum:
        second_maximum = maximum
        maximum = n
    elif n > second_maximum:
        second_maximum = n

print(second_maximum)
