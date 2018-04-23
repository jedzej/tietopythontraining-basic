input_data = input().split(' ')
for row in range(0, len(input_data)):
    input_data[row] = int(input_data[row])
min_val = input_data.index(min(input_data))
max_val = input_data.index(max(input_data))
input_data[min_val], input_data[max_val] = \
    input_data[max_val], input_data[min_val]
list_to_str = [str(a) for a in input_data]
list_str = " ".join(list_to_str)
print(list_str)
