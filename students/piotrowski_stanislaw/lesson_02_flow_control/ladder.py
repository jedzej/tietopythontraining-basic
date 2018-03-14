# https://snakify.org/lessons/for_loop_range/problems/ladder/
# piotrsta

num = int(input())

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print('')
