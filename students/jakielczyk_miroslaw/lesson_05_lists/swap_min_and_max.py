list_of_numbers = input().split(' ')
for x in range(len(list_of_numbers)):
    list_of_numbers[x] = int(list_of_numbers[x])
index_min = list_of_numbers.index(min(list_of_numbers))
index_max = list_of_numbers.index(max(list_of_numbers))
list_of_numbers[index_min], list_of_numbers[index_max] = list_of_numbers[index_max], list_of_numbers[index_min]
for element in list_of_numbers:
    print(element, end=' ')
