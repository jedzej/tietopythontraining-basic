# The sequence consists of distinct positive integer numbers and ends with
# the number 0. Determine the value of the second largest element in this
# sequence. It is guaranteed that the sequence has at least two elements.

first = int(input())
second = int (input())


if first < second:
    first, second = second, first
seq_element = second

while seq_element != 0:
    seq_element = int(input())
    if seq_element > first:
        second = first
        first = seq_element
    if first > seq_element > second:
        second = seq_element
else:
    print("Second maximum is " + str(second))
