print("Enter integer:")
a = int(input())

units = a % 10
tens = int(((a % 100) - units) / 10)
hundreds = int(((a % 1000) - tens - units) / 100)

digit_sum = units + tens + hundreds

print("Sum: " + str(digit_sum))

