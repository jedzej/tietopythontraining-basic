#A sequence consists of integer numbers and ends with the number 0. Determine how
#many elements of this sequence are equal to its largest element. 

import sys

print("Enter the sequence:")

n=-1
largest = 0
equal_elements = 1;

while n != 0:
    n = int(input())

    #increase the number of largest equals apart from when there
    # is only 0 in the sequence
    if (largest == n) and (n != 0):
        equal_elements = equal_elements + 1
    if (n > largest):
        largest = n
        equal_elements = 1


print("number of elements equal to sequence's largest element:")
print(equal_elements)
