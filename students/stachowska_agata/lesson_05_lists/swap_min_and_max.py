n = [int(i) for i in input().split()]

min_n = n[0]
max_n = n[0]

for i in n:
    if i > max_n:
        max_n = i

    elif i < min_n:
        min_n = i

min_pos = n.index(min_n)
max_pos = n.index(max_n)

n[min_pos] = max_n
n[max_pos] = min_n

print(' '.join(str(i) for i in n))
