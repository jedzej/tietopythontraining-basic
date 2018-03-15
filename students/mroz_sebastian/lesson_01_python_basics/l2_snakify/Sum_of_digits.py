a = int(input())

sum_of_digits = a % 10 + a % 100 // 10 + a // 100
print(sum_of_digits)
