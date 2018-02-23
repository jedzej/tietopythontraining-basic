number = int(input())

digit1 = number // 100
digit2 = number // 10 % 10
digit3 = number % 10

print(digit1 + digit2 + digit3)