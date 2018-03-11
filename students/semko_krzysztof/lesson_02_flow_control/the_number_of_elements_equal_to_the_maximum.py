"""
A sequence consists of integer numbers and ends with the number 0.
Determine how many elements of this sequence are equal to its largest element.
"""

print("Please input integers in a sequence. to finish, type '0'.")
loop_number = 1
max_value = 0
max_count = 0
while loop_number > 0:
    value = int(input())
    if loop_number > 2:
        if value == 0:
            loop_number = 0
            break

    if value == max_value:
        max_count += 1

    if value > max_value:
        max_value = value
        max_count = 1
    loop_number += 1

print("Number of integers with max value (" + str(max_value) + ") = " + str(max_count))
