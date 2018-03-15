#https://snakify.org/lessons/print_input_numbers/problems/apple_sharing/
#piotrsta

n = int(input('Ilu uczniow: '))
k = int(input('Ile jablek: '))

applesPerStud = k // n
print('Uczen dostanie ' + str(applesPerStud) + ' jablek')
remainInBasket = k % n
print('W koszu zostanie ' + str(remainInBasket) + ' jablek')
