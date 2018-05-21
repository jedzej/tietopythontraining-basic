#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
#The program reads the numbers N and K. It should print the two answers for the questions above.

# Read the numbers like this:
N = int(input())    # number of students
K = int(input())    # number of apples
# Example of division, integer division and remainder:
print(K // N)       # apples per student
print(K % N)        # apples left
