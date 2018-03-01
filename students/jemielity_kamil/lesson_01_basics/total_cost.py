import math
dollars = int(input('How many dollars: '))
cents = int(input('How many cents: '))
numberOfCupcakes = int(input('Number of cupcake: '))

wallet = str(dollars) + '.' + str(cents)
costOfCupcakes = float(wallet) * numberOfCupcakes
print(str(costOfCupcakes).split('.')[0] + " " + str(costOfCupcakes).split('.')[1])


