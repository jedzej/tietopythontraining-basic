import math

first_class = int(input("Write how many students are in first class: "))
second_class = int(input("Write how many students are in second class: "))
third_class = int(input("Write how many students are in third class: "))

desks_in_first_class = math.ceil(first_class/2)
desks_in_second_class = math.ceil(second_class/2)
desks_in_third_class = math.ceil(third_class/2)

total_desks = desks_in_first_class + desks_in_second_class + desks_in_third_class

print("Total number of desks: " + str(total_desks))

