# Given N numbers: the first number in the input is N, after that N integers are given.
# Count the number of zeros among the given integers and print it.

# You need to count the number of numbers that are equal to zero, not the number of zero digits.

total_count = int(input())

result = 0

for _ in range(total_count):
    if int(input()) == 0:
        result += 1

print(result)
