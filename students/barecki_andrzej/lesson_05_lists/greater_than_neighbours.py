input_list = input().split(' ')
greater_counter = 0
for row in range(1, len(input_list) - 1):
    if input_list[row - 1] < input_list[row] and\
            input_list[row] > input_list[row + 1]:
        greater_counter += 1

print(greater_counter)
