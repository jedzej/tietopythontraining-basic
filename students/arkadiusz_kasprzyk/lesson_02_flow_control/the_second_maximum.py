"""
description:
    The sequence consists of distinct positive integer numbers and ends with the number 0.
    Determine the value of the second largest element in this sequence.
    It is guaranteed that the sequence has at least two elements.
"""

print("""
    The sequence consists of distinct positive integer numbers and ends with the number 0. 
    Determine the value of the second largest element in this sequence. 
""")

n = int(input("give the first number : "))

max = n
max2 = 0

if n>0:
    while n > 0:
        n = int(input("give the next number : "))
        if n > max:
            max2 = max
            max = n
        elif n > max2:
            max2 = n
        else:
            pass
    print(max2)

else:
    print("The first number must be > 0.")
