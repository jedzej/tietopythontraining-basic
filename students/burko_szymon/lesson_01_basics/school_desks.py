import math
a = int(input("Number of students in class a: "))
b = int(input("Number of students in class b: "))
c = int(input("Number of students in class c: "))

desks_in_a = math.ceil(a / 2)
desks_in_b = math.ceil(b / 2)
desks_in_c = math.ceil(c / 2)

all_desks = desks_in_a + desks_in_b + desks_in_c

print("The smallest possible number of desks: " + str(all_desks))
