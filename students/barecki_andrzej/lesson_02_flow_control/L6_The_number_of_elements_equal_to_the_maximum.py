# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are
#  equal to its largest element.

input_number = int(input())

maximum = 0
max_elements_nr = 0
while input_number:
    if input_number > maximum:
        max_elements_nr = 1
        maximum = input_number
    elif input_number == maximum:
        max_elements_nr += 1
    input_number = int(input())

print(max_elements_nr)
