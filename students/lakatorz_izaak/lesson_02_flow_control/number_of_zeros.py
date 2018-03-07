# Given N numbers: the first number in the input is N, after that N integers
#  are given. Count the number of zeros among the given integers and print it.

print("Enter number of integers")
amount = int(input())

zeros_amount = 0

for i in range(0, amount):
    amount = int(input())
    if amount == 0:
        zeros_amount += 1

print(zeros_amount)
