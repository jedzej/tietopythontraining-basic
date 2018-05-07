input_str = input()
input_list = input_str.split()

index_of_max = 0
index_of_min = 0

for i in range(0, len(input_list)):
    if int(input_list[i]) > int(input_list[index_of_max]):
        index_of_max = i
    if int(input_list[i]) < int(input_list[index_of_min]):
        index_of_min = i

tmp = input_list[index_of_max]
input_list[index_of_max] = input_list[index_of_min]
input_list[index_of_min] = tmp
print(input_list)
