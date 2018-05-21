#The sequence consists of distinct positive integer numbers and ends with the
#number 0. Determine the value of the second largest element in this sequence. It
#is guaranteed that the sequence has at least two elements.

import sys

print("Enter the sequence:")

n=-1
largest = 0
second_largest=0
aux_count = 0;

while n != 0:
    aux_count = aux_count + 1
    n = int(input())

    if (n < 0):
        print("Error: negative value")
        sys.exit()
    if(aux_count == 1) and (n == 0):
        print("Error: sequence not long enough")
        sys.exit()

    if (n > largest):
        second_largest = largest
        largest = n

print("The second largest is:")
print(second_largest)
