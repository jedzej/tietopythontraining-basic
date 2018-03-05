first_max = 0
n = int(input())
while n != 0:
    if n > first_max:
        second_max, first_max = first_max, n
    elif n > second_max:
        second_max = n
    n = int(input())

print(second_max)
