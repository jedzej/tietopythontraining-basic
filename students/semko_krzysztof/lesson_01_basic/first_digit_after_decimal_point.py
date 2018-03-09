# Problem «First digit after decimal point» (Easy)
# Statement
# Given a positive real number, print its first digit to the right of the decimal point.

print('Please input a number with floating point:')
val = float(input())
print('First digit after decimal point: ' + str(int(val * 10) % 10))
