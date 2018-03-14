print("School desks\n")

a = int(input("Enter the number of students in the first grade: "))
b = int(input("Enter the number of students in the second grade: "))
c = int(input("Enter the number of students in the third grade: "))

class1 = (a // 2) + (a % 2)
class2 = (b // 2) + (b % 2)
class3 = (c // 2) + (c % 2)

d = class1 + class2 + class3

print("\nThe school must buy %d desks" %d)