biggest = 0
second_biggest = 0
while True:
    n = int(input())
    if n > biggest:
        second_biggest = biggest
        biggest = n
    if (n > second_biggest) and (n != biggest):
        second_biggest = n
    if n == 0:
        break
print(second_biggest)
