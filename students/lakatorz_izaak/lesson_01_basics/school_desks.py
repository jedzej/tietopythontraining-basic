from math import ceil

print("Enter number of students in class a:")
class_a = int(input())

print("Enter number of students in class b:")
class_b = int(input())

print("Enter number of students in class c:")
class_c = int(input())

desks = ceil(class_a/2) + ceil(class_b/2) + ceil(class_c/2)

print ("Smallest possible number of desks is equal to " + str(desks))