# lesson_01_basics
# School desks

# Statement
# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks
# that can be purchased.
#
# The program should read three integers: the number of students in each of the three classes,
# a, b and c respectively.

print("Enter the number of sudents in the first classroom")
a = int(input())
xa = (a + 1) // 2

print("Enter the number of sudents in the second classroom")
b = int(input())
xb = (b + 1) // 2

print("Enter the number of sudents in the third classroom")
c = int(input())
xc = (c + 1) // 2

xt = xa + xb + xc
print("The total number of required desks is: " + str(xt) + ".")


