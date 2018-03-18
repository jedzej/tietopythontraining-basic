dol = int(input('How many dolars for a cupcakes?\n'))
cent = int(input('How many cents for a cupcakes?\n'))
n = int(input('How many cupcakes do you need?\n'))
cost100 = (dol * 100 + cent) * n
print('You need to pay ' + str(cost100//100) + ' dolars and ' + str(cost100 % 100 ) + ' cents\n')
