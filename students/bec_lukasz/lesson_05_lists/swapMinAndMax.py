my_list = input('Input your list: ').split()

min_index = 0
max_index = 0

for i in range(1, len(my_list)):
    if int(my_list[i]) > int(my_list[max_index]):
        max_index = i
    if int(my_list[i]) < int(my_list[min_index]):
        min_index = i

my_list[min_index], my_list[max_index] = my_list[max_index], my_list[min_index]

for i in range(len(my_list)):
    print(my_list[i], end=' ')
