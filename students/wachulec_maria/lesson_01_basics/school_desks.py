a = int(input("Amount of students in first class: "))
b = int(input("Amount of students in second class: "))
c = int(input("Amount of students in third class: "))

desks_for_a = a // 2 + a % 2
desks_for_b = b // 2 + b % 2
desks_for_c = c // 2 + c % 2

print(desks_for_a + desks_for_b + desks_for_c)
