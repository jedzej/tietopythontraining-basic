import math

N = int(input("Number of students: "))
K = int(input("Amount of apples: "))

amountOfApplesPerStudent = math.floor(K/N)
otherApples = K - (amountOfApplesPerStudent * N)

print("Each student will get: " + str(amountOfApplesPerStudent) + " apples")
print("Number of apples that remain in the basket: " + str(otherApples))
