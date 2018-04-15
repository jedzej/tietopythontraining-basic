in_list = [int(i) for i in input().split()]

max_val = in_list.index(max(in_list))
min_val = in_list.index(min(in_list))

in_list[min_val], in_list[max_val] = in_list[max_val], in_list[min_val]

print(' '.join([str(i) for i in in_list]))
