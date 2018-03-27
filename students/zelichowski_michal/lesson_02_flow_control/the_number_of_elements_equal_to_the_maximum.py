"""A sequence consists of integer numbers and ends with the number 0.
Determine how many elements of this sequence are equal to its largest
element. """

a = int(input())
maxi = 0
number_of_max = 0
while a != 0:
    if a > maxi:
        maxi = a
        number_of_max = 1
    elif a == maxi:
        number_of_max += 1
    a = int(input())
print(number_of_max)
