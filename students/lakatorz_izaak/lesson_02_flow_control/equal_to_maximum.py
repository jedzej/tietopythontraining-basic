#A sequence consists of integer numbers and ends with the number 0.
#Determine how many elements of this sequence are equal to its largest element.

seq_element = int(input())
largest = seq_element
amount_of_max = 1

while seq_element != 0:
    seq_element = int(input())

    if seq_element == largest:
        amount_of_max += 1
    if seq_element > largest:
        largest = seq_element
        amount_of_max = 1
else:
    print(str(amount_of_max) + " elements are equal to largest.")
