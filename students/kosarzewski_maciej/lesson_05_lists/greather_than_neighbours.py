input_data = input().split(' ')
counter = 0
for x in range(1, len(input_data) - 1):
    if input_data[x - 1] < input_data[x] \
            and input_data[x] > input_data[x + 1]:
        counter += 1
print(counter)
