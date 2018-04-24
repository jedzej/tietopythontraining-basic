l = []
k = 0

while True:
    n = int(input('n' + str(k + 1) + ' = '))
    k += 1

    if n == 0 and k > 2:
        break
    else:
        l.append(n)

l_sorted = sorted(l, reverse=True)

print('\n', l_sorted[1])
