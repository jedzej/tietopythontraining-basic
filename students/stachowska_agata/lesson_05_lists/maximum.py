m, n = (int(i) for i in input().split())

array = []

for i in range(m):
    array.append([int(x) for x in input().split()])

max_value = array[0][0]
x_max = 0
y_max = 0

for x in range(m):
    for y in range(n):
        if array[x][y] > max_value:
            max_value = array[x][y]
            x_max, y_max = [x, y]

print(x_max, y_max)
