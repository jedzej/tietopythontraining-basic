# Problem «Tens digit» (Medium)
# Statement
# Given an integer. Print its tens digit.

print('Please input integer number:')
val = int(input())
print('Tens number = ' + str((val % 100) // 10))
