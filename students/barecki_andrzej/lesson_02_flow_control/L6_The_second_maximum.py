# The sequence consists of distinct positive integer numbers and ends with the number 0. Determine the value of the
# second largest element in this sequence. It is guaranteed that the sequence has at least two elements.


maximum = 0
second_maximum = 0
while True:
    input_number = int(input())
    if input_number == 0:
        break
    if input_number > maximum:
        second_maximum = maximum
        maximum = input_number
    elif input_number > second_maximum:
        second_maximum = input_number

print(second_maximum)
