# https://snakify.org/lessons/while_loop/problems/seq_num_maximal/
# piotrsta

max_val = 0
num_of_max_val = 0

while True:
    number = int(input())

    if number >= max_val:
        if number > max_val:
            num_of_max_val = 0
        max_val = number
        num_of_max_val += 1

    if number == 0:
        break
print(num_of_max_val)
