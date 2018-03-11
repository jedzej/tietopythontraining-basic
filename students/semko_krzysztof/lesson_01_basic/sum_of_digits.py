# Problem «Sum of digits» (Medium)
# Statement
# Given a three-digit number. Find the sum of its digits.

print('Please give a three digit number:')
val = int(input())
print('Sum of numbers = ' + str((val // 100) + (val % 100 // 10) + (val % 10)))
