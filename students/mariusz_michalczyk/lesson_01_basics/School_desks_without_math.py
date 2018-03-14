students_of_A_class = int(input("Enter number of students for class A: "))
students_of_B_class = int(input("Enter number of students for class B: "))
students_of_C_class = int(input("Enter number of students for class C: "))

def get_desks(students):
    desks = 0
    if students % 2 == 0:
        desks = students // 2
    else:
        desks = (students // 2) + 1
    return desks

total = get_desks(students_of_A_class) + get_desks(students_of_B_class) + get_desks(students_of_C_class)
print ("Total nr of desks: " + str(total))


