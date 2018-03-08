from math import ceil

students_of_A_class = int(input("Enter number of students for class A: "))
students_of_B_class = int(input("Enter number of students for class B: "))
students_of_C_class = int(input("Enter number of students for class C: "))

total = ceil(students_of_A_class / 2) + ceil(students_of_B_class / 2) + ceil(students_of_C_class / 2)

print ("Total nr of desks: " + total)


