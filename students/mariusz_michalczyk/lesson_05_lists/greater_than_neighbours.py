def get_quantity(input_string):
    list_of_nrs = input_string.split()
    quantity = 0
    for i in range(1, len(list_of_nrs) - 1):
        if list_of_nrs[i - 1] < list_of_nrs[i] > list_of_nrs[i + 1]:
            quantity += 1
    return quantity


input_string = input()
print(get_quantity(input_string))
