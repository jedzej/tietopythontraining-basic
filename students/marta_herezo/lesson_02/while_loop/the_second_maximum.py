# The sequence consists of distinct positive integer
# numbers and ends with the number 0.
print('Enter numbers: ')

num1 = int(input())
num2 = int(input())

if num1 < num2:
    num1, num2 = num2, num1

element = int(input())
while element != 0:
    if element > num1:
        num2, num1 = num1, element
    elif element > num2:
        num2 = element
    element = int(input())
print(num2)
