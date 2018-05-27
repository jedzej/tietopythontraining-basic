a = [int(x) for x in input().split()]
minimum = a[0]
maximum = a[0]
min_index = 0
max_index = 0

for i in range(len(a)):
    if a[i] < minimum:
        minimum = a[i]
        min_index = i
    if a[i] > maximum:
        maximum = a[i]
        max_index = i

a[max_index], a[min_index] = a[min_index], a[max_index]

for i in range(len(a)):
    print(a[i], end=" ")
