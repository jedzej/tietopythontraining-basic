# calculate factorial of number

number = int(input())
factorial = 1

while number:
    factorial = factorial * number
    number = number - 1

print(factorial)
