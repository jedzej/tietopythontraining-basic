import math

n = int(input("Number of students: "))
k = int(input("Amount of apples: "))

amount_of_apples_per_student = math.floor(k/n)
other_apples = k - (amount_of_apples_per_student * n)

print("Each student will get: " + str(amount_of_apples_per_student) + " apples")
print("Number of apples that remain in the basket: " + str(other_apples))
