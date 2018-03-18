# A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students
# in each class, print the smallest possible number of desks that can be purchased.
#
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

a = int(input())
b = int(input())
c = int(input())
print(a//2 + b//2 + c//2 + a%2 + b%2 + c%2)
