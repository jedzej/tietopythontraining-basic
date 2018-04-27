int_list = input("Enter a list of integer numbers separated by space: ")
new_list = int_list.split()

quantity = 0
if len(new_list) >= 3:
    for i in range(1, len(new_list) - 1):
        if new_list[i] > new_list[i - 1] and \
                new_list[i] > new_list[i + 1]:
            quantity += 1
print("Number of elements greater than neighbours: ", quantity)
