# Problem «Total cost» (Medium)
# Statement
# A cupcake costs A dollars and B cents. Determine, how many dollars and cents
# should one pay for N cupcakes. A program gets three numbers: A, B, N.
# It should print two numbers: total cost in dollars and cents.

print('Please input cost of 1 piece in dollars part:')
dollars = int(input())
print('Please input cost of 1 piece in cents part:')
cents = int(input())
print('Please input number of cupcakes:')
number = int(input())

print('Total cost = ' + str((dollars * number) + int((cents * number) / 100)) + ' dollars, ' +
      str((cents * number / 100) % 1) + ' cents.')
