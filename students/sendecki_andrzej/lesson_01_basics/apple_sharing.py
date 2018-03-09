# lesson_01_basics
# Apple sharing
#
# Statement
# N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get?
# How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above. 

print("Enter the number of students")
N = int(input())
print("Enter the number of apples")
K = int(input())

xN = K // N
xK = K % N

print("Each student will get " + str(xN) + " apple(s).")
print("There will be " + str(xK) + " apple(s) left in the basket.")

