#https://snakify.org/lessons/while_loop/problems/seq_second_max/
#piotrsta

max1 = 0
max2 = 0

while True:
    number = int(input())
    if number > max1:
        max2 = max1
        max1 = number
    elif number > max2:
        max2 = number

    if number == 0:
        break
print(max2)
