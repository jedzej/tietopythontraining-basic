# Problem «School desks» (Hard)
# Statement
# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#
# In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

from math import ceil

print("please input size of first group:")
first = int(input())
print("please input size of second group:")
second = int(input())
print("please input size of third group:")
third = int(input())

print('Number needed: ' + str(ceil(first / 2) + ceil(second / 2) + ceil(third / 2)))
