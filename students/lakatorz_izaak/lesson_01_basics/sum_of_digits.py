print("Enter integer:")
a = int(input())

digit_sum = 0

while a > 0:
    digit = a % 10
    digit_sum = digit_sum + digit
    a = int(a/10)

print("Sum: " + str(digit_sum))
