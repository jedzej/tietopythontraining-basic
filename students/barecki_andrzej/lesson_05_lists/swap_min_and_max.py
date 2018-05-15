input_list = input().split(' ')
for row in range(0, len(input_list)):
    input_list[row] = int(input_list[row])
min_index = input_list.index(min(input_list))
max_index = input_list.index(max(input_list))
input_list[min_index], input_list[max_index] = \
    input_list[max_index], input_list[min_index]
print(input_list)
