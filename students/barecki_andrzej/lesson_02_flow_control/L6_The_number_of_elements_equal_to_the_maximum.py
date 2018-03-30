# A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are
#  equal to its largest element.

maximum = 0
max_elements_nr = 0
while True:
    input_number = int(input())
    if input_number == 0:
        break
    if input_number > maximum:
        max_elements_nr = 1
        maximum = input_number
    elif input_number == maximum:
        max_elements_nr += 1

print(max_elements_nr)
