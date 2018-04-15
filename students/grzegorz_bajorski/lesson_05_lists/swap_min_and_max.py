input_list = [int(i) for i in input().split()]

max_val = input_list.index(max(input_list))
min_val = input_list.index(min(input_list))

input_list[min_val], input_list[max_val] = input_list[max_val], input_list[min_val]

print(' '.join([str(i) for i in input_list]))
