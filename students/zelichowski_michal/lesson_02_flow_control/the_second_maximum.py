"""The sequence consists of distinct positive integer numbers
and ends with the number 0. Determine the value of the second largest
element in this sequence. It is guaranteed that the sequence has at least
two elements. """

a = int(input())
maxi = 0
second_max = 0
while a != 0:
    if a > maxi:
        second_max = maxi
        maxi = a
    elif a <= maxi:
        if a > second_max:
            second_max = a
    a = int(input())

print(second_max)
