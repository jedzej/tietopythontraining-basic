#Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 

def find_min(my_list):
    min_num = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] < min_num:
            min_num = my_list[i]

    return min_num

def find_max(my_list):
    max_num = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]

    return max_num


numbers = [1, 2, 6, 4, 5, 8, 0, -9, 3]

print("Original list")
print(numbers)

min_index = numbers.index(find_min(numbers))
min_number = find_min(numbers)
max_index = numbers.index(find_max(numbers))
max_number = find_max(numbers)

numbers[min_index] = max_number
numbers[max_index] = min_number

print("Re-ordered list")
print(numbers)
