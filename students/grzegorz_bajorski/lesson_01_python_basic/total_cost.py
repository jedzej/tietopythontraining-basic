print('Enter dollars cost')
dollars = int(input())

print('Enter cents cost')
cents = int(input())

print('Enter number of cupcakes')
cupcakes = int(input())

total =int((dollars * 100 + cents) * cupcakes)

print('total cost in dollars and cents is ' + str(total// 100) + ' ' + str(total % 100))

