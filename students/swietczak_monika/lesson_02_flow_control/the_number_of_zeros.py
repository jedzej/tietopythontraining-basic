# Read an integer:
n = int(input("How many numbers? "))
sum_of_zeros = 0

for i in range(n):
    number = int(input("Enter a number: "))
    if number == 0:
        sum_of_zeros += 1
# Print a value:
print(sum_of_zeros)
