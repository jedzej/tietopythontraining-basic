import math
dollars = int(input('How many dollars: '))
cents = int(input('How many cents: '))
number_of_cupcakes = int(input('Number of cupcake: '))

wallet = str(dollars) + '.' + str(cents)
cost_of_cupcakes = float(wallet) * number_of_cupcakes
print(str(cost_of_cupcakes).split('.')[0] + " " + str(cost_of_cupcakes).split('.')[1])

