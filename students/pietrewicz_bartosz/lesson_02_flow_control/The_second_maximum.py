# Read the numbers until 0 is read and remember 2 greatest numbers
maximum = 0
second_maximum = 0
n = 1
while n != 0:
    n = int(input())
    if n > maximum:
        maximum, second_maximum = n, maximum
    elif (n <= maximum) and (n > second_maximum):
        second_maximum = n
print(second_maximum)
