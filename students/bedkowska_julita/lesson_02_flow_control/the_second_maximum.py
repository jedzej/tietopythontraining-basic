the_largest = int(input())
the_second_largest = int(input())
if the_second_largest > the_largest:
    the_largest, the_second_largest = the_second_largest, the_largest
i = int(input())
while i != 0:
    if i > the_largest:
        the_second_largest, the_largest = the_largest, i
    elif i > the_second_largest:
        the_second_largest = i
    i = int(input())

print('{} {}'.format('The second largest number is:', the_second_largest))
