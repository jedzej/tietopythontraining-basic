'''
title: apple_sharing
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    N students take K apples and distribute them among each other evenly.
    The remaining (the undivisible) part remains in the basket.
    How many apples will each single student get?
    How many apples will remain in the basket?

    The program reads the numbers N and K.
    It should print the two answers for the questions above.
'''

print('''N students take K apples and distribute them among each other evenly.
    The remaining (the undivisible) part remains in the basket.
    How many apples will each single student get?
    How many apples will remain in the basket?
'''
)

N = int(input("Give number of students: "))
K = int(input("Give number of apples: "))

k = K // N
r = K % N

print("Each student obtain {} apples.".format(k))
print("{} apples will be left.".format(r))


input("Press Enter to quit the program.")