array_size = input()
n = int((array_size.split(' '))[0])
m = int((array_size.split(' '))[1])
entry_array = []
for x in range(n):
    entry_array.append(input().split(' '))
rows = len(entry_array)
columns = len(entry_array[0])
maximum = int(entry_array[rows - 1][columns - 1])
coordinate_x = rows - 1
coordinate_y = columns - 1
for row in range(rows):
    for column in range(columns):
        element = int(entry_array[rows - row - 1][columns - column - 1])
        if element >= maximum:
            maximum = element
            coordinate_y = columns - column - 1
            coordinate_x = rows - row - 1
print(coordinate_x, coordinate_y)
