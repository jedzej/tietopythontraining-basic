biggest = 0
sum_number = 0
while True:
    n = int(input())
    if n > biggest:
        sum_number = 1
        biggest = n
    elif biggest == n:
        sum_number += 1
    if n == 0:
        break
print(sum_number)
