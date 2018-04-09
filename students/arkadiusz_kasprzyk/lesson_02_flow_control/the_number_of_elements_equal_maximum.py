"""
description:
    A sequence consists of integer numbers and ends with the number 0.
    Determine how many elements of this sequence are equal to its largest element.
"""

print("""
    A sequence consists of integer numbers and ends with the number 0. 
    Determines how many elements of this sequence are equal to its largest element.
""")

n = int(input("give the first number : "))

max = n
counter = 1

if n>0:
    while n > 0:
        n = int(input("give the next number : "))
        if n > max:
            max = n
            counter = 1
        elif n == max:
            counter += 1
        else:
            pass
    print("Maximum is {} and there is {} elements equal to it.".format(max, counter))

else:
    print("The first number must be > 0.")
