

n, k = [int(i) for i in input('Numbers: ').split()]
bowls = ['I' for i in range(n)]

for x in range(k):
    range_a, range_b = [int(i) for i in input('Pins: ').split()]

    for i in range(range_a, range_b+1):
        bowls[i-1] = '.'

bowls = ''.join(bowls)
print(bowls)
