element_of_list = [int(i) for i in input("Type number and press SPACE."
                                         "\nOnce you want to end - press ENTER. ").split()]

quantity_of_elements_greater_than_sum_of_neighbors = 0

for i in range(1, len(element_of_list) - 1):
    if element_of_list[i - 1] < element_of_list[i] > element_of_list[i + 1]:
        quantity_of_elements_greater_than_sum_of_neighbors += 1

print(quantity_of_elements_greater_than_sum_of_neighbors)

