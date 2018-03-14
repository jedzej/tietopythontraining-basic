# Problem «Apple sharing» (Medium)
# Statement
# N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
#
# The program reads the numbers N and K. It should print the two answers for the questions above.
print('Input students number:')
students = int(input())
print('Input number of apples:')
apples = int(input())
print('Apples per student: ' + str(apples // students))
print('Apples left: ' + str(apples % students))
