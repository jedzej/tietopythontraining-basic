print('enter real number')

digit = float(input())

real_digit, frac_digit = str(digit).split(".")

print('First digit of fractional part is ' + str(frac_digit[0]))
