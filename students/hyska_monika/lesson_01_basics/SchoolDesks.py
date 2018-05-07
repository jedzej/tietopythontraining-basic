# This program returns previous and next numbers for integer number

a = int(input("Put number of students in a class: "))
b = int(input("Put number of students in b class: "))
c = int(input("Put number of students in c class: "))

desc_a = (a // 2) + (a % 2)
desc_b = (b // 2) + (b % 2)
desc_c = (c // 2) + (c % 2)

desc= desc_a + desc_b + desc_c

print("Number of desc needed to buy:", desc)