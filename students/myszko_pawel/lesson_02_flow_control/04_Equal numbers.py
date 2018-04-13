# Given three integers, determine how many of them are equal to each other.
# The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

a = int(input())
b = int(input())
c = int(input())

counter = 0
if a == b == c:
    counter = 3
elif (a == b) or (a == c) or (b == c):
    counter = 2
print(counter)
