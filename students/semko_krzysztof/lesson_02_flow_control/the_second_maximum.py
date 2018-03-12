"""
The sequence consists of distinct positive integer numbers
and ends with the number 0.
Determine the value of the second largest element in this sequence.
It is guaranteed that the sequence has at least two elements.
"""

print("Please input integers in a sequence. to finish, type '0'.")

max_value = 0
second_max = 0
while True:
    value = int(input())

    if max_value > 0 and second_max > 0 and value == 0:
        break

    if value > max_value:
        second_max = max_value
        max_value = value
    elif value > second_max:
        second_max = value

print("Second to max value = " + str(second_max))
