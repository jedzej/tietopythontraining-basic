digit = int(input())
hundreds = digit // 100
tens = (digit % 100 - digit % 10) // 10
ones = digit % 10

print(hundreds + tens + ones)
