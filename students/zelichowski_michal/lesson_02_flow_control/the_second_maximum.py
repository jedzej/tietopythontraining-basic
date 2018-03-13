"""The sequence consists of distinct positive integer numbers
and ends with the number 0. Determine the value of the second largest
element in this sequence. It is guaranteed that the sequence has at least
two elements. """

a = int(input())
max = 0
secondMax = 0
while a != 0:
    if a > max:
        secondMax = max
        max = a
    elif a <= max:
        if a > secondMax:
            secondMax = a
    a = int(input())

print(secondMax)

