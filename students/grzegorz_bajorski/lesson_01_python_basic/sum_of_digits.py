print('enter 3 digit number')

digit = int(input())

sum_digit = int((digit // 100 ) + ((digit % 100)/10 ) + (digit % 10 ))

print('Sum of digits is ' + str(sum_digit))
