from math import ceil
# Read an integer:
class1 = int(input("Provide number of students in class 1: "))
class2 = int(input("Provide number of students in class 2: "))
class3 = int(input("Provide number of students in class 3: "))
# Print a value:
a = ceil((class1 / 2)) + ceil((class2 / 2)) + ceil((class3 / 2))
print(a)
