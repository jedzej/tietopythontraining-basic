created_list = [int(s) for s in input("Create list of numbers by typing the number and SPACE"
                           "\n If you wish to finish - press ENTER: ").split()]

index_of_min = 0
index_of_max = 0

for i in range(1, len(created_list)):
    if created_list[i] > created_list[index_of_max]:
        index_of_max = i
    if created_list[i] < created_list[index_of_min]:
        index_of_min = i

created_list[index_of_min], created_list[index_of_max] = created_list[index_of_max], created_list[index_of_min]

print(' '.join([str(i) for i in created_list]))